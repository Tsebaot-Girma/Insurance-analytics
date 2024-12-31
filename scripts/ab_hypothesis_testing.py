from scipy.stats import ttest_ind, f_oneway
import pandas as pd

def t_test(group_a, group_b, alpha=0.05):
    """Perform a t-test between two groups"""
    t_stat, p_value = ttest_ind(group_a, group_b)
    result = "reject" if p_value < alpha else "fail to reject"
    return t_stat, p_value, result

def anova_test(groups, alpha=0.05):
    """Perform ANOVA test for multiple groups"""
    f_stat, p_value = f_oneway(*groups)
    result = "reject" if p_value < alpha else "fail to reject"
    return f_stat, p_value, result

def test_risk_differences_across_provinces(df, alpha=0.05):
    """Test risk differences across provinces"""
    provinces = df['Province'].unique()
    groups = [df[df['Province'] == province]['TotalClaims'] for province in provinces]
    
    f_stat, p_value, result = anova_test(groups, alpha)
    
    print(f"ANOVA Test for Risk Differences Across Provinces:")
    print("Null Hypothesis: No risk differences across provinces")
    print(f"F-Statistic: {f_stat}")
    print(f"P-Value: {p_value}")
    print(f"Result: {result} the null hypothesis")
def test_risk_differences_between_zipcodes(df, zip_code_a, zip_code_b, alpha=0.05):
    """Test risk differences between two zip codes"""
    zip_a_data = df[df['PostalCode'] == zip_code_a]['TotalClaims']
    zip_b_data = df[df['PostalCode'] == zip_code_b]['TotalClaims']
    
    t_stat, p_value, result = t_test(zip_a_data, zip_b_data, alpha)
    
    print(f"T-Test for Risk Differences Between Zip Codes {zip_code_a} and {zip_code_b}:")
    print("Null Hypothesis: No risk differences between zip codes")
    print(f"T-Statistic: {t_stat}")
    print(f"P-Value: {p_value}")
    print(f"Result: {result} the null hypothesis")
def test_profit_differences_between_zipcodes(df, zip_code_a, zip_code_b, alpha=0.05):
    """Test profit differences between two zip codes"""
    df['ProfitMargin'] = df['TotalPremium'] - df['TotalClaims']
    
    zip_a_profit = df[df['PostalCode'] == zip_code_a]['ProfitMargin']
    zip_b_profit = df[df['PostalCode'] == zip_code_b]['ProfitMargin']
    
    t_stat, p_value, result = t_test(zip_a_profit, zip_b_profit, alpha)
    
    print(f"T-Test for Profit Differences Between Zip Codes {zip_code_a} and {zip_code_b}:")
    print("Null Hypothesis: No significant margin differences between zip codes")
    print(f"T-Statistic: {t_stat}")
    print(f"P-Value: {p_value}")
    print(f"Result: {result} the null hypothesis")
def test_risk_differences_between_genders(df, alpha=0.05):
    """Test risk differences between Women and Men"""
    women_data = df[df['Gender'] == 'Female']['TotalClaims']
    men_data = df[df['Gender'] == 'Male']['TotalClaims']
    
    t_stat, p_value, result = t_test(women_data, men_data, alpha)
    
    print(f"T-Test for Risk Differences Between Women and Men:")
    print("Null Hypothesis: No significant risk differences between women and men")
    print(f"T-Statistic: {t_stat}")
    print(f"P-Value: {p_value}")
    print(f"Result: {result} the null hypothesis")
