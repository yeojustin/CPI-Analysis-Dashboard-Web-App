import pandas as pd
import streamlit as st

PATH = "datasets/"

@st.cache_data
def load_bop_cpi_merged():
    df = pd.read_csv(f"{PATH}cpibop_merged.csv")
    df['Year'] = df['Year'].astype(int)
    return df

@st.cache_data
def load_cpi_yearly():
    df_yearly = pd.read_csv(f"{PATH}cpi-yearly.csv", index_col=0)
    df_yearly.index = df_yearly.index.astype(str)
    print("Yearly Data Index:", df_yearly.index)
    return df_yearly

@st.cache_data
def load_cpi_quarterly():
    df_quarterly = pd.read_csv(f"{PATH}cpi-quarterly.csv", index_col=0)
    df_quarterly.index = df_quarterly.index.astype(str)
    print("Quarterly Data Index:", df_quarterly.index)
    return df_quarterly

@st.cache_data
def load_cpi_halfyearly():
    df_halfyearly = pd.read_csv(f"{PATH}cpi-halfyearly.csv", index_col=0)
    # df_halfyearly.index = pd.to_datetime(df_halfyearly.index, errors='coerce').strftime('%Y-%H')
    df_halfyearly.index = df_halfyearly.index.astype(str)
    print("Halfyearly Data Index:", df_halfyearly.index)
    return df_halfyearly

@st.cache_data
def load_cpi_yearly_pct():
    df_yearly_pct = pd.read_csv(f"{PATH}cpi-yearly-pct.csv", index_col=0)
    df_yearly_pct.index = df_yearly_pct.index.astype(str)
    print("Yearly Data Index:", df_yearly_pct.index)
    return df_yearly_pct

@st.cache_data
def load_cpi_quarterly_pct():
    df_quarterly_pct = pd.read_csv(f"{PATH}cpi-quarterly-pct.csv", index_col=0)
    df_quarterly_pct.index = df_quarterly_pct.index.astype(str)
    print("Quarterly Data Index:", df_quarterly_pct.index)
    return df_quarterly_pct

@st.cache_data
def load_cpi_halfyearly_pct():
    df_halfyearly_pct = pd.read_csv(f"{PATH}cpi-halfyearly-pct.csv", index_col=0)
    # df_halfyearly.index = pd.to_datetime(df_halfyearly.index, errors='coerce').strftime('%Y-%H')
    df_halfyearly_pct.index = df_halfyearly_pct.index.astype(str)
    print("Halfyearly Data Index:", df_halfyearly_pct.index)
    return df_halfyearly_pct

# Define category structure
def get_categories_struct():
    return {
        "All Items": [],
        "Food": [],
        "Food Excl Food Serving Services": {
            "Bread & Cereals": [
                "Rice",
                "Flour",
                "Bread",
                "Noodles & Pasta",
                "Biscuits & Cookies",
                "Cakes & Pastries",
                "Other Cereals"
            ],
            "Meat": [
                "Pork, Chilled",
                "Beef, Chilled",
                "Mutton, Chilled",
                "Poultry, Chilled",
                "Meat, Frozen",
                "Meat Preparations"
            ],
            "Fish & Seafood": [
                "Fish, Chilled",
                "Fish, Frozen",
                "Other Seafood",
                "Seafood Preparations"
            ],
            "Milk, Cheese & Eggs": [
                "Formula Milk Powder",
                "Other Milk & Dairy Products",
                "Eggs"
            ],
            "Oils & Fats": [
                "Butter & Other Fats",
                "Cooking Oils"
            ],
            "Fruits": [
                "Tropical Fruits, Fresh",
                "Citrus, Berries & Other Fruits, Fresh",
                "Preserved Fruits & Nuts"
            ],
            "Vegetables": [
                "Leafy Vegetables, Fresh",
                "Fruit Vegetables, Fresh",
                "Root Vegetables, Fresh",
                "Other Vegetables & Preparations"
            ],
            "Sugar, Preserves & Confectionery": [
                "Sugar",
                "Confectionery & Ice-cream",
                "Sugar Preserves & Spread"
            ],
            "Non-alcoholic Beverages": [
                "Coffee & Tea",
                "Soft Drinks",
                "Other Beverages"
            ],
            "Other Food": []
        },
        ## End of Food Excl Food Serving Services

        "Food Serving Services": {
            "Restaurant Food": [],
            "Fast Food": [],
            "Hawker Food": {
                "Hawker Centres": [],
                "Food Courts & Coffee Shops": []
            },
            "Catered Food": []
        },
        # End of food serving services

        "Clothing & Footwear": {
            "Clothing": {
                "Men's Clothing": [],
                "Women's Clothing": [],
                "Children's Clothing": []
            },
            "Other Articles & Related Services": [],
            "Footwear": {
                "Men's Footwear": [],
                "Women's Footwear": [],
                "Children's Footwear": []
            },
            "Housing & Utilities": {
                "Accommodation3": [],
                "Utilities & Other Fuels": [
                    "Water Supply",
                    "Refuse Collection",
                    "Electricity",
                    "Gas"
                ]
            },
            "Household Durables & Services": {
                "Household Durables": [
                    "Furniture",
                    "Furnishings",
                    "Other Household Textiles",
                    "Household Appliances",
                    "Utensils & Others"
                ],
                "Household Services & Supplies": [
                    "Non-durable Household Goods",
                    "Domestic & Household Services"
                ]
            }
        },
        # End of clothing & footwear

        "Health Care": {
            "Medicines & Health Products": [
                "Medicines & Vitamins",
                "Medical Products"
            ],
            "Outpatient Services": [
                "Fees At Polyclinics",
                "Fees At General Practitioners (GP) Clinics",
                "Fees At Specialist Outpatient Clinics",
                "Dental Services",
                "Paramedical Services"
            ],
            "Hospital Services": [],
            "Health Insurance": []
        },
        # End of healthcare

        "Transport": {
            "Private Transport": [
                "Cars",
                "Motorcycles",
                "Petrol",
                "Other Private Transport"
            ],
            "Public Transport": [
                "Bus & Train Fares",
                "Point-to-point Transport Services2",
                "Other Public Transport"
            ],
            "Other Transport Services": [
                "Air Fares",
                "Other Transport"
            ]
        }, 
        # End of clothing & footwear

        "Communication": [
            "Postage & Courier Services",
            "Telecommunication Equipment",
            "Telecommunication Services"
        ], 
        # End of Communication

        "Recreation & Culture": {
            "Recreational & Cultural Goods": [
                "Information Processing Equipment",
                "Audio-visual Equipment & Others",
                "Games & Toys",
                "Pets & Related Products",
                "Other Recreational & Cultural Goods"
            ],
            "Recreational & Cultural Services": [
                "Sport Services & Other Fees",
                "Cinema Tickets",
                "Charges To Places Of Interest",
                "Other Recreational & Cultural Services"
            ],
            "Newspapers, Books & Stationery": [
                "Newspapers & Magazines",
                "Books & Stationery"
            ],
            "Holiday Expenses": [
                "Package Tours",
                "Hotels & Other Expenses"
            ]
        }, 
        # End of Recreation & Culture

        "Education": {
            "Tuition & Other Fees": [
                "Primary Education",
                "Secondary Education",
                "Other General, Vocational & Higher Education",
                "Enrichment & Supplementary Courses"
            ],
            "Textbooks & Study Guides": []
        },
        # End of education 

        "Miscellaneous Goods & Services": {
            "Personal Care": [
                "Hairdressing",
                "Personal Grooming Services",
                "Other Personal Care"
            ],
            "Alcoholic Drinks & Tobacco": [
                "Spirits & Wine",
                "Beer",
                "Cigarettes"
            ],
            "Personal Effects": [
                "Jewellery & Watches",
                "Other Personal Effects"
            ],
            "Social Services": [],
            "Other Miscellaneous Services": []
        },
        # End of Misc

        "All Items Less Imputed Rentals On Owner-occupied Accommodation3": [],
        "All Items Less Accommodation3": []
    }

# Function to get Level 1 keys
def get_L1_keys():
    return [key for key in get_categories_struct()]

# Function to get Level 2 keys
def get_L2_keys():
    L2_keys = []
    categories_struct = get_categories_struct()
    for L1_key in get_L1_keys():
        if isinstance(categories_struct[L1_key], dict):
            L2_keys.extend(categories_struct[L1_key].keys())
    return L2_keys

# Function to get all unique keys from the nested structure
def get_all_keys():
    all_keys = set()

    def traverse_categories(struct):
        for key, value in struct.items():
            all_keys.add(key)
            if isinstance(value, dict):
                traverse_categories(value)
            elif isinstance(value, list):
                all_keys.update(value)

    # Traverse CPI categories
    traverse_categories(get_categories_struct())

    # Traverse BOP categories
    traverse_categories(get_bop_categories_struct())

    return list(all_keys)

# Define BOP category structure
def get_bop_categories_struct():
    return {
        "D Overall Balance (A-B+C)": {
            "A Current Account Balance": {
                "Goods Balance": ["Exports Of Goods","Imports Of Goods"],
                "Services Balance": {
                    "Exports Of Services": {
                        "Manufacturing Services On Physical Inputs Owned By Others": [],
                        "Maintenance And Repair Services": [],
                        "Transport": [
                            "Freight",
                            "Others"
                        ],
                        "Travel": [],
                        "Insurance": [],
                        "Government Goods And Services": [],
                        "Construction": [],
                        "Financial": [],
                        "Telecommunications, Computer & Information": [],
                        "Charges For The Use Of Intellectual Property": [],
                        "Personal, Cultural And Recreational": [],
                        "Other Business Services": [
                            "Accounting",
                            "Advertising And Market Research",
                            "Architectural",
                            "Business Management",
                            "Engineering And Technical",
                            "Legal",
                            "Research And Development",
                            "Operating Leasing",
                            "Trade-Related",
                            "Others"
                        ]
                    },
                    "Imports Of Services": {
                        "Manufacturing Services On Physical Inputs Owned By Others": [],
                        "Maintenance And Repair Services": [],
                        "Transport": [
                            "Freight",
                            "Others"
                        ],
                        "Travel": [],
                        "Insurance": [],
                        "Government Goods And Services": [],
                        "Construction": [],
                        "Financial": [],
                        "Telecommunications, Computer & Information": [],
                        "Charges For The Use Of Intellectual Property": [],
                        "Personal, Cultural And Recreational": [],
                        "Other Business Services": [
                            "Accounting",
                            "Advertising And Market Research",
                            "Architectural",
                            "Business Management",
                            "Engineering And Technical",
                            "Legal",
                            "Research And Development",
                            "Operating Leasing",
                            "Trade-Related",
                            "Others"
                        ]
                    }
                },
                "Primary Income Balance": [
                    "Primary Income Receipts",
                    "Primary Income Payments"
                ],
                "Secondary Income Balance": [
                    "Secondary Income Receipts",
                    "Secondary Income Payments"
                ]
            },
            "B Capital & Financial Account Balance": {
                "Financial Account (Net)": {
                    "Direct Investment": [
                        "Assets",
                        "Liabilities"
                    ],
                    "Portfolio Investment": {
                        "Assets": [
                            "Deposit-Taking Corporations, Except The Central Bank",
                            "Official",
                            "Others"
                        ],
                        "Liabilities": [
                            "Deposit-Taking Corporations, Except The Central Bank",
                            "Others"
                        ]
                    },
                    "Financial Derivatives": [
                        "Assets",
                        "Liabilities"
                    ],
                    "Other Investment": {
                        "Assets": [
                            "Deposit-Taking Corporations, Except The Central Bank",
                            "Official",
                            "Others"
                        ],
                        "Liabilities": [
                            "Deposit-Taking Corporations, Except The Central Bank",
                            "Others"
                        ]
                    }
                }
            },
            "C Net Errors & Omissions": {},
            "E Reserve Assets": [
                "Special Drawing Rights",
                "Reserves Position In The IMF",
                "Foreign Exchange Assets"
            ]
        }
    }

def get_bop_L1_keys():
    return [key for key in get_bop_categories_struct()]

def get_bop_L2_keys():
    L2_keys = []
    categories_struct = get_bop_categories_struct()
    if "D Overall Balance (A-B+C)" in categories_struct:
        for L2_key, L2_value in categories_struct["D Overall Balance (A-B+C)"].items():
            if isinstance(L2_value, dict):
                L2_keys.append(L2_key)
    return L2_keys

def get_bop_L3_keys(L1_key, L2_key):
    L3_keys = []
    categories_struct = get_bop_categories_struct()
    if L1_key in categories_struct and L2_key in categories_struct[L1_key]:
        L3_value = categories_struct[L1_key][L2_key]
        if isinstance(L3_value, dict):
            for L3_key in L3_value:
                L3_keys.append(L3_key)
    return L3_keys

def get_bop_L1_keys():
    categories_struct = get_bop_categories_struct()
    return list(categories_struct.keys())



if __name__ == "__main__":
    print(get_bop_L1_keys())
    print("Passed")
    print(get_bop_L2_keys())
    print("Passed")
    # print(get_bop_L3_keys())
    # print("Passed")

    print("All Keys in CPI Categories:", get_all_keys())
    print("Passed")
