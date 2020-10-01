#
# This is the code we thought we were going to use until we realized we could expand the number of terms in the search
#
# 1 INITIALIZATION

# import SearchSampler script from Pew Code
from search_sampler import SearchSampler

# add Google Health Trends API key (Corinne)
apikey = 'AIzaSyBa1PTogBywoug3ALLlHT2DWaffrpip39k'

# add Google Health Trends API key (Susan)
#apikey = 'AIzaSyDXG4pZyO3c0GAsQ9nEk0puaUZKwlTRpco'

# define where to save output samples
output_path = 'C:\\Users\\Krist\\Box Sync\\Google-search-data\\Child-Maltreatment-Search\\Search B - w hotline and signs\\Sample 7'

#output_path = 'C:\\Users\\Krist\\Box Sync\\Google-search-data\\Child-Maltreatment-Search\\Search C - Add sex with me\\Just 2019'

# tell the rolling window how many samples to pull. For this purposes of this project, we are pulling one at a time
num_samples = 1




# ENTER SEARCH REGION HERE

states = ['US-AK', 'US-AL', 'US-AR','US-AZ','US-CA', 'US-CO', 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI', 'US-IA', 'US-ID', 'US-IL', 'US-IN','US-KS', 'US-KY', 'US-LA', 'US-MA','US-MD', 'US-ME', 'US-MI', 'US-MN','US-MO', 'US-MS', 'US-MT', 'US-NC', 'US-ND', 'US-NE', 'US-NH', 'US-NJ','US-NM', 'US-NV', 'US-NY', 'US-OH','US-OK', 'US-OR', 'US-PA', 'US-RI','US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VA', 'US-VT', 'US-WA','US-WI', 'US-WV', 'US-WY'],

#We started running samples until we realized we were going to expand the search term
#Sample 1
#States Ran 7/17: 'US-AK', 'US-AL', 'US-AR','US-AZ','US-CA', 'US-CO', 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI', 'US-IA', 'US-ID', 'US-IL', 'US-IN','US-KS', 'US-KY', 'US-LA', 'US-MA','US-MD', 'US-ME', 'US-MI', 'US-MN','US-MO', 'US-MS', 'US-MT', 'US-NC', 'US-ND', 'US-NE', 'US-NH', 'US-NJ','US-NM', 'US-NV', 'US-NY', 'US-OH'
#States Ran 7/18: 'US-OK','US-OR', 'US-PA', 'US-RI','US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VA', 'US-VT', 'US-WA','US-WI', 'US-WV', 'US-WY'

#Sample 2
#States Ran 7/18: 'US-AK', 'US-AL', 'US-AR','US-AZ','US-CA', 'US-CO', 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI', 'US-IA', 'US-ID', 'US-IL', 'US-IN','US-KS', 'US-KY', 'US-LA', 'US-MA','US-MD', 'US-ME'
#States Ran 7/20: 'US-MI', 'US-MN','US-MO', 'US-MS', 'US-MT', 'US-NC', 'US-ND', 'US-NE', 'US-NH', 'US-NJ','US-NM', 'US-NV', 'US-NY', 'US-OH','US-OK', 'US-OR', 'US-PA', 'US-RI','US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VA', 'US-VT'
#States Ran 7/21: 'US-WA','US-WI', 'US-WV', 'US-WY'

#Sample 3
#States Ran 7/21: 'US-AK', 'US-AL', 'US-AR','US-AZ','US-CA', 'US-CO', 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI','US-IA', 'US-ID', 'US-IL', 'US-IN','US-KS', 'US-KY', 'US-LA', 'US-MA','US-MD', 'US-ME'
#States Ran 7/22: 'US-MI', 'US-MN','US-MO', 'US-MS', 'US-MT', 'US-NC', 'US-ND', 'US-NE', 'US-NH', 'US-NJ','US-NM', 'US-NV', 'US-NY', 'US-OH','US-OK', 'US-OR', 'US-PA', 'US-RI','US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VA', 'US-VT', 'US-WA','US-WI', 'US-WV', 'US-WY'

#Sample 4
#States Ran 7/22: 'US-AK', 'US-AL', 'US-AR','US-AZ','US-CA', 'US-CO'
#States Ran 7/23: 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI', 'US-IA', 'US-ID', 'US-IL', 'US-IN','US-KS', 'US-KY', 'US-LA', 'US-MA','US-MD', 'US-ME', 'US-MI', 'US-MN','US-MO', 'US-MS', 'US-MT', 'US-NC', 'US-ND', 'US-NE', 'US-NH', 'US-NJ','US-NM', 'US-NV', 'US-NY', 'US-OH','US-OK', 'US-OR', 'US-PA', 'US-RI','US-SC', 'US-SD'
#States Ran 7/26: 'US-TN', 'US-TX', 'US-UT', 'US-VA', 'US-VT', 'US-WA','US-WI', 'US-WV', 'US-WY'

#Sample 5
#States Ran 7/26: 'US-AK', 'US-AL', 'US-AR','US-AZ','US-CA', 'US-CO', 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI', 'US-IA', 'US-ID', 'US-IL', 'US-IN','US-KS', 'US-KY', 'US-LA', 'US-MA','US-MD', 'US-ME', 'US-MI', 'US-MN','US-MO', 'US-MS', 'US-MT'
#States Ran 7/27: 'US-NC', 'US-ND', 'US-NE', 'US-NH', 'US-NJ','US-NM', 'US-NV', 'US-NY', 'US-OH','US-OK', 'US-OR', 'US-PA', 'US-RI','US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VA', 'US-VT', 'US-WA','US-WI', 'US-WV', 'US-WY'

#Sample 6
#States Ran 7/28: 'US-AK', 'US-AL', 'US-AR','US-AZ','US-CA', 'US-CO', 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI', 'US-IA', 'US-ID', 'US-IL', 'US-IN','US-KS', 'US-KY', 'US-LA', 'US-MA','US-MD', 'US-ME', 'US-MI', 'US-MN','US-MO', 'US-MS', 'US-MT', 'US-NC', 'US-ND', 'US-NE', 'US-NH', 'US-NJ','US-NM', 'US-NV', 'US-NY', 'US-OH'
#States Ran 7/29: 'US-OK', 'US-OR', 'US-PA', 'US-RI','US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VA', 'US-VT', 'US-WA','US-WI', 'US-WV', 'US-WY'

#Sample 7
#States Ran 7/29: 'US-AK', 'US-AL', 'US-AR','US-AZ','US-CA', 'US-CO', 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI', 'US-IA', 'US-ID', 'US-IL', 'US-IN','US-KS', 'US-KY', 'US-LA', 'US-MA','US-MD'

# 2. FUNCTIONS

# function for changing df format from long to wide and renaming some columns
# Note this was not in the original Pew code, but is necessary so the data work with the R code.
# Since we are only pulling one sample at a time, we are not using this function at this time
def reformatFile(df):
    # use pandas built in pivot to change general format from long to wide
    df = df.pivot(index='timestamp', columns='sample', values='value')
    # rename columns by appending "sample_" as a prefix to each
    df.columns = ["sample_" + str(col) for col in df.columns]
    # create column name to hold each period
    df.index.name = "period"
    # move period values from index list to actual column inside df
    df.reset_index(inplace=True)
    # convert from date_time to just date
    df['period'] = df['period'].dt.date
    return df


# function taking in list of region codes and path to save data to
def query(regionCodes, filePath):
    # for each region in the input regionCodes list passed as a parameter
    for region in regionCodes:
        # Print the name of the region for verbosity
        print("running search for following region: ", region)
        # search params
        params = {

            #Search terms we were considering

            #Final "Search B" - the combo search with only 30 terms. It includes 'child abuse hotline' and 'signs of abuse'
            'search_term': ["mom hit me + dad hit me + mother hit me + father hit me + mom hurt me + dad hurt me + mother hurt me + father hurt me + afraid of mom + afraid of dad + afraid of mother + afraid of father + mom hate me + dad hate me + mother hate me + father hate me + mom is high + dad is high + mother is high + father is high + mom passed out + dad passed out + mother passed out + father passed out + mom touch my + dad touch my + mother touch my + father touch my + child abuse hotline + signs of child abuse"],

            #Search A  - the combo search with only 28 terms. It removed 'child abuse hotline' and 'signs of abuse'
             #'search_term': ["mom hit me + dad hit me + mother hit me + father hit me + mom hurt me + dad hurt me + mother hurt me + father hurt me + afraid of mom + afraid of dad + afraid of mother + afraid of father + mom hate me + dad hate me + mother hate me + father hate me + mom is high + dad is high + mother is high + father is high + mom passed out + dad passed out + mother passed out + father passed out + mom touch my + dad touch my + mother touch my + father touch my"],

            #Search C - the combo search with 30 terms. It replaced hotline/signs with "[mom/dad] have sex with me
             #'search_term': ["mom hit me + dad hit me + mother hit me + father hit me + mom hurt me + dad hurt me + mother hurt me + father hurt me + afraid of mom + afraid of dad + afraid of mother + afraid of father + mom hate me + dad hate me + mother hate me + father hate me + mom is high + dad is high + mother is high + father is high + mom passed out + dad passed out + mother passed out + father passed out + mom touch my + dad touch my + mother touch my + father touch my + mom have sex with me + dad have sex with me"],


            # Search Region is defined by State variable above.
            'region': region,

            # Must be in format YYYY-MM-DD
            'period_start': '2017-12-31',
            'period_end': '2020-07-11',

            # Options are day, week, month.
            'period_length': 'week'
        }

        sample = SearchSampler(apikey, "child-maltreatment-search-b", params, output_path=filePath)

        # GETTING DATA

        # single sample:
        # df_results = sample.pull_data_from_api()
        # save results:
        # sample.save_file(df_results['Both terms test'])

        # rolling set of samples. For the purposes of this project we are pulling one sample at a time, so this is 1.
        df_results = sample.pull_rolling_window(num_samples=num_samples)
        # df_results = reformatFile(df_results)
        sample.save_file(df_results, append=True)


# call query for all states
query(regionCodes=states, filePath=output_path + "/states")

