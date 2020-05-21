#1 INITIALIZATION

# import SearchSampler script from Pew Code
from search_sampler import SearchSampler

# add Google Health Trends API key (Corinne)
apikey = 'AIzaSyBa1PTogBywoug3ALLlHT2DWaffrpip39k'

#Eli's key
#apikey = 'AIzaSyCfSZJnyW37oJy6dUzMZuONWwN77v8Mtbw'

# define where to save output samples
output_path = 'C:\\Users\\Krist\\Box Sync\\Google-search-data\\NewSearches\\Cornavirus Symptoms'

# tell the rolling window how many samples to pull.
# if doing single sample pull, this number doesn't seem to do anything
num_samples = 1

# list of all state codes so search_sampler will be able to run script on all states.
# can only pull 4 states each day
'''states = ['US-AL', 'US-AK', 'US-AZ', 'US-AR']'''
'''states = ['US-CA', 'US-CO', 'US-CT', 'US-DC']'''
'''states = ['US-DE', 'US-FL', 'US-GA', 'US-HI']'''
'''states = ['US-ID', 'US-IL', 'US-IN', 'US-IA']'''
'''states = ['US-KS', 'US-KY', 'US-LA', 'US-ME']'''
'''states = ['US-MD', 'US-MA', 'US-MI']'''
'''states = ['US-MN', 'US-MS', 'US-MO', 'US-MT']'''
'''states = ['US-NE', 'US-NV', 'US-NH', 'US-NJ']'''
'''states = ['US-NM', 'US-NY', 'US-NC', 'US-ND']'''
'''states = ['US-OH', 'US-OK', 'US-OR', 'US-PA']'''
'''states = ['US-RI', 'US-SC', 'US-SD', 'US-TN']'''
'''states = ['US-TX', 'US-UT', 'US-VT', 'US-VA']'''
'''states = ['US-WA', 'US-WV', 'US-WI', 'US-WY']'''
''' Can pull entire US at once with states = 'US'  '''

'''states = ['US']'''

'''states = ['US-AL', 'US-AK', 'US-AZ', 'US-AR', 'US-CA', 'US-CO', 'US-CT', 'US-DC','US-DE', 'US-FL', 'US-GA', 'US-HI',
'US-ID', 'US-IL', 'US-IN', 'US-IA','US-KS', 'US-KY', 'US-LA', 'US-ME','US-MD', 'US-MA', 'US-MI','US-MN', 'US-MS', 'US-MO', 
'US-MT', 'US-NE', 'US-NV', 'US-NH', 'US-NJ','US-NM', 'US-NY', 'US-NC', 'US-ND','US-OH', 'US-OK', 'US-OR', 'US-PA','US-RI', 
'US-SC', 'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VT', 'US-VA', 'US-WA', 'US-WV', 'US-WI', 'US-WY']'''

states = ['US-AL', 'US-AK', 'US-AZ', 'US-AR', 'US-CA', 'US-CO', 'US-CT', 'US-DC']

# list of all DMA codes
'''dmas = []'''

# 2. FUNCTIONS

# function for changing df format from long to wide and renaming some columns
# Note this was not in the original Pew code, but is necessary so the data work with the R code.
def reformatFile(df):
   # use pandas built in pivot to change general format from long to wide
   df = df.pivot(index='timestamp', columns='sample', values='value')
   # rename columns by appending "sample_" as a prefix to each
   df.columns = ["sample_"+str(col) for col in df.columns]
   # create column name to hold each period
   df.index.name="period"
   # move period values from index list to actual column inside df
   df.reset_index(inplace=True)
   # convert from date_time to just date
   df['period'] = df['period'].dt.date
   return df

#function taking in list of region codes and path to save data to
def query(regionCodes, filePath):
   # for each region in the input regionCodes list passed as a parameter
   for region in regionCodes:
       # Print the name of the region for verbosity
       print("running search for following region: ", region)
       # search params
       params = {
       # Can be any number of search terms, using boolean logic. See report methodology for more info.

       #'search_term':['covid', 'coronavirus'],
       #'search_term':['mom makes me scared + mom made me scared + I am scared of mom + I\'m scared of mom + dad makes me scared + dad made me scared + I am scared of dad + I\'m scared of dad'],
        'search_term': ['coronavirus symptoms + covid symptoms + covid-19 symptoms + covid19 symptoms + corona symptoms'],

       # Can be country, state, or DMA. States are US-CA. DMA are a 3 digit code; see Nielsen for info.
       'region':region,

       # Must be in format YYYY-MM-DD
       'period_start': '2020-01-01',
       'period_end': '2020-04-30',

       # Options are day, week, month. WARNING: This has been extensively tested with week only.
       'period_length':'day'
       }

       sample = SearchSampler(apikey, "cornavirus symptoms variations", params, output_path=filePath)

       # GETTING DATA

       # single sample:
       #df_results = sample.pull_data_from_api()
        #save results:
       #sample.save_file(df_results['Both terms test'])

       # rolling set of samples:
       df_results = sample.pull_rolling_window(num_samples=num_samples)
       #df_results = reformatFile(df_results)
       sample.save_file(df_results, append=True)


# call query for all states
query(regionCodes=states, filePath=output_path+"/states")

# call query for all DMAs
# query(regionCodes=dmas, filePath=output_path+"/dmas")
