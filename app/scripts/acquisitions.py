import pandas as pd
import numpy as np

class AcquisitionAssumptions:

    def __init__(self):
        pass


xlsx = pd.ExcelFile("model_riverbend_apartments.xlsx")
df_assumptions = pd.read_excel(xlsx, "assumptions")
df_rent_roll = pd.read_excel(xlsx, "rent roll")

df = df_assumptions.set_index('Fields').to_dict()['Assumptions']
prop_name = df["PROJECT NAME"]
prop_address = df["PROPERTY ADDRESS"]
prop_county = df["COUNTY"]
prop_market = df["MARKET "]
units_per_acre = df["ACREAGE - UNITS PER ACRE"]
total_parking_spots = df["TOTAL PARKING SPOTS"]
year_built = df["APPROXIMATE YEAR BUILT"]
num_buildings = df["NUMBER OF BUILDINGS "]
asking_price = df["ASKING PRICE"]
occupancy = df["OCCUPANCY"]
y1_vacancy = df["YEAR 1 VACANCY"]
y1_vacancy_change = df["VACANCY CHANGE Y1"]
y2_vacancy_change = df["VACANCY CHANGE Y2"]
y3_vacancy_change = df["VACANCY CHANGE Y3"]
y4_vacancy_change = df["VACANCY CHANGE Y4"]
y5_vacancy_change = df["VACANCY CHANGE Y5"]
market_rent_growth_y1 = df["MARKET RENT GROWTH Y1"]
market_rent_growth_y1 = df["MARKET RENT GROWTH Y2"]
market_rent_growth_y1 = df["MARKET RENT GROWTH Y3"]
market_rent_growth_y4 = df["MARKET RENT GROWTH Y4"]
market_rent_growth_y5 = df["MARKET RENT GROWTH Y5"]
reno_rent_increase_y1 = df["RENOVATION INCREASE Y1"]
reno_rent_increase_y2 = df["RENOVATION INCREASE Y2"]
reno_rent_increase_y3 = df["RENOVATION INCREASE Y3"]
reno_rent_increase_y4 = df["RENOVATION INCREASE Y4"]
reno_rent_increase_y5 = df["RENOVATION INCREASE Y5"]
other_income_increase_y1 = df["OTHER INCOME INCREASE Y1"]
other_income_increase_y2 = df["OTHER INCOME INCREASE Y2"]
other_income_increase_y3 = df["OTHER INCOME INCREASE Y3"]
other_income_increase_y4 = df["OTHER INCOME INCREASE Y4"]
other_income_increase_y5 = df["OTHER INCOME INCREASE Y5"]
prop_tax_rate = df["TAX RATE"]
prop_tax_assess_rate = df["TAX ASSESS PER"]
mortgage_amort_term_y1 = df["MORTGAGE AMORT TERM Y1"]
mortgage_amort_term_y2 = df["MORTGAGE AMORT TERM Y2"]
mortgage_amort_term_y3 = df["MORTGAGE AMORT TERM Y3"]
mortgage_amort_term_y4 = df["MORTGAGE AMORT TERM Y4"]
mortgage_amort_term_y5 = df["MORTGAGE AMORT TERM Y5"]
mortgage_maturity_term_y1 = df["MORTGAGE MAT TERM Y1"]
mortgage_maturity_term_y2 = df["MORTGAGE MAT TERM Y2"]
mortgage_maturity_term_y3 = df["MORTGAGE MAT TERM Y3"]
mortgage_maturity_term_y4 = df["MORTGAGE MAT TERM Y4"]
mortgage_maturity_term_y5 = df["MORTGAGE MAT TERM Y5"]
LTV = df["LTV"]
ten_yr_treasury = df["10 YR TREASURY"]
ten_yr_treasury_spread = df["EST SPREAD"]
commission_fee = df["POINTS/COMMISSION FEE RATE"]
investor_pref_return_y1 = df["INVESTOR PREF RETURN Y1"]
investor_pref_return_y2 = df["INVESTOR PREF RETURN Y2"]
investor_pref_return_y3 = df["INVESTOR PREF RETURN Y3"]
investor_pref_return_y4 = df["INVESTOR PREF RETURN Y4"]
investor_pref_return_y5 = df["INVESTOR PREF RETURN Y5"]
cashflow_participation = df["CASH FLOW PARTICIPATION PER"]
asset_management_fee = df["ASSET MANAGEMENT FEE"]
T12_Other_Income = df["OTHER INCOME"]
T12_Utility_Income = df["UTILITY INCOME (SEWER/ELECTRICITY/ETC.)"]
T12_Utility_Income_other = df["UTILITY INCOME (PEST/TRASH)"]
T12_Admin_and_Application_Fees = df["ADMIN & APPLICATION FEE"]
T12_Late_Fees = df["LATE FEES, FORFEITED DEPOSITS, TERMINATION FEE"]
T12_Ancillary_Income = df["ANCILLARY INCOME"]
T12_Corporate_Units = df["CORPORATE UNITS"]
T12_Delinquent_Units = df["DELINQUENT RENT"]
T12_Non_Revenue_Units = df["NON-REVENUE UNITS"]
T12_Concessions = df["CONCESSIONS"]
T12_Loss_to_Lease = df["LOSS TO LEASE"]
T12_Insurance = df["INSURANCE"]
T12_Utilities = df["UTILITIES"]
T12_Marketing = df["MARKETING"]
T12_Service_Contracts = df["SERVICE CONTRACTS (+ PEST & TRASH)"]
T12_Exterior = df["EXTERIOR & GROUND - REPAIRS & MAINTENANCE "]
T12_Payroll = df["PAYROLL"]
T12_Management_Fee = df["MANAGEMENT FEE"]
T12_Turnover = df["INTERIOR REPAIRS - TURNOVER"]
T12_SGA = df["GENERAL, ADMIN, & LICENSES/FEES/PERMITS"]
T12_Reserves = df["RESERVES (NEW APPL, VINYL, CARPET)"]
T12_Rent_Per_Market = df["PERCENT OF MARKET"]
T12_90_Day_Trailing = df["90-DAY TRAILING"]








print