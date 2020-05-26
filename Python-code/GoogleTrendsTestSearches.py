# 1 INITIALIZATION

# import SearchSampler script from Pew Code
from search_sampler import SearchSampler

# add Google Health Trends API key (Corinne)
apikey = 'AIzaSyBa1PTogBywoug3ALLlHT2DWaffrpip39k'

# define where to save output samples
output_path = 'C:\\Users\\Krist\\Box Sync\\Google-search-data\\NewSearches\\Weather'

# tell the rolling window how many samples to pull.
# if doing single sample pull, this number doesn't seem to do anything
num_samples = 1

# list of all state codes so search_sampler will be able to run script on all states. Some options include

# Some options include:
    # states = ['US-AK', 'US-AL', 'US-AR','US-AZ']
    # states = ['US-CA', 'US-CO', 'US-CT', 'US-DC']
    # states = ['US-DE', 'US-FL', 'US-GA', 'US-HI']
    # states = ['US-IA', 'US-ID', 'US-IL', 'US-IN']
    # states = ['US-KS', 'US-KY', 'US-LA', 'US-MA']
    # states = ['US-MD', 'US-ME', 'US-MI', 'US-MN']
    # states = ['US-MO', 'US-MS', 'US-MT', 'US-NC']
    # states = ['US-ND', 'US-NE', 'US-NH', 'US-NJ']
    # states = ['US-NM', 'US-NV', 'US-NY', 'US-OH']
    # states = ['US-OK', 'US-OR', 'US-PA', 'US-RI']
    # states = ['US-SC', 'US-SD', 'US-TN', 'US-TX']
    # states = ['US-UT', 'US-VA', 'US-VT', 'US-WA']
    # states = ['US-WI', 'US-WV', 'US-WY']

states = ['US-AL', 'US-AK', 'US-AZ', 'US-AR', 'US-CA', 'US-CO', 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI',
'US-ID', 'US-IL', 'US-IN', 'US-IA','US-KS', 'US-KY', 'US-LA', 'US-ME','US-MD', 'US-MA', 'US-MI','US-MN', 'US-MS', 'US-MO', 
'US-MT', 'US-NE', 'US-NV', 'US-NH', 'US-NJ','US-NM', 'US-NY', 'US-NC', 'US-ND','US-OH', 'US-OK', 'US-OR', 'US-PA','US-RI', 
'US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VT', 'US-VA', 'US-WA', 'US-WV', 'US-WI', 'US-WY']

    # Can pull entire US at once with :  states = ['US']'''


# ENTER SEARCH REGION HERE
#states = ['US']

# list of all DMA codes
'''dmas = []'''


# 2. FUNCTIONS

# function for changing df format from long to wide and renaming some columns
# Note this was not in the original Pew code, but is necessary so the data work with the R code.
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

            # Can be any number of search terms, using boolean logic. See report methodology for more info.

            # Searches previously executed:

            # COVID Related Searches
                # Ran on 4/27 - 4/29  : ['covid', 'coronavirus']
                # Ran on 4/29 - 5/1 : ['corona']
                # Ran on 5/11 : ['coronavirus'], ['symptoms'], ['coronavirus', 'symptoms'], ['coronavirus symptoms'], ['coronavirus' + 'symptoms'], ['coronavirus' + ' symptoms'], ["coronavirus  symptoms"], ['coronavirus + symptoms'], ['coronavirus' + 'symptoms'], ['coronavirus' and 'symptoms'] [coronavirus' or 'symptoms]
                # Ran on 5/20 - 5/22 : ['coronavirus symptoms + covid symptoms + covid-19 symptoms + covid19 symptoms + corona symptoms']

            # Unemployment Searches
                #Ran on 4/26 - 4/27: ['unemployment']

            # Child Abuse initial tests (Ran on 5/15)
                # ['bruises on baby + baby concussion]
                # ['Child protective services + Child protective service']
                # ['mom makes me afraid + mom made me afraid + I am afriad of mom + I'm afraid of dad + dad makes me afraid + dad made me afraid + I am afriad of dad + I'm afraid of dad']
                # ['mom makes me scared + mom made me scared + I am scared of mom + I\'m scared of mom + dad makes me scared + dad made me scared + I am scared of dad + I\'m scared of dad']
                # ['mom passed out + dad passed out']
                # ['dad touched my + dad forced me to + molested me']
                # ['dad beat me + dad beats me + mom beat me + mom beats me + dad hurts me + dad hurt me + mom hurts me + mom hurt me']
                # ['mom hit me + mom slapped me + mom slap me + mom push me + mom hurt me + dad hit me + dad slapped me + dad slap me + dad push me + dad hurt me']

            #Domestic Abuse initial tests (Ran on 5/15)
                # ['Abuse hotline + Abuse help + Abuse emergency line + abuse helpline + abuse support line + abuse support + domestic violence hotline + domestic violence help + domestic violence helpline + domestic violence support + domestic violence support line']
                # ['I feel unsafe + makes me feel unsafe']
                # ['How to leave abusive marriage + how to get out of bad relationship + how to get out of abusive relationship + how to leave abusive relationship + how to get out of dangerous relationship + how to leave dangerous relationship']
                # ['husband hit me + husband beat me + husband slapped me + husband kicked me + husband punched me + husband choked me + husband strangled me + boyfriend hit me + boyfriend beat me + boyfriend slapped me + boyfriend kicked me + boyfriend punched me + boyfriend choked me + boyfriend strangled me]
                # ['Find women's shelter + find domestic violence shelter + women shelter near me + women's shelter near me + help for abused women + emergency number for domestic violence + domestic violence emergency help' ]

            #Baseline Searches
                #Weekly Weather Queries, ran on 5/25: ['weather']

            # CURRENT SEARCH
            'search_term': ['weather'],

            # Can be country, state, or DMA. States are US-CA. DMA are a 3 digit code; see Nielsen for info.
            'region': region,

            # Must be in format YYYY-MM-DD
            'period_start': '2019-01-01',
            'period_end': '2019-12-31',

            # Options are day, week, month. WARNING: This has been extensively tested with week only.
            'period_length': 'daily'
        }

        sample = SearchSampler(apikey, "weather", params, output_path=filePath)

        # GETTING DATA

        # single sample:
        # df_results = sample.pull_data_from_api()
        # save results:
        # sample.save_file(df_results['Both terms test'])

        # rolling set of samples:
        df_results = sample.pull_rolling_window(num_samples=num_samples)
        # df_results = reformatFile(df_results)
        sample.save_file(df_results, append=True)


# call query for all states
query(regionCodes=states, filePath=output_path + "/states")

# call query for all DMAs
# query(regionCodes=dmas, filePath=output_path+"/dmas")
