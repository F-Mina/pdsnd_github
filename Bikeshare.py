import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Initially asking the user specify a ctiy, month and day to analyse.
def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # Getting user input for city (chicago, new york city, washington). 

    city = input("Please choose one those cities: Chicago, New York city, Washington:\n").lower()

    while (city not in city):

        city = input("Which city do you want explore?").lower()
    print("Chicago", "New York", "Washington")
    
    # Getting user input for month (all, january, february, ... , june)
        
    month = input("Please choose one those monhts:\n").lower()
    months = ["all", "january", "february", "march", "april", "may", "june"]
    while (month not in months):
        month = input("Please choose one those monhts").lower()
        print("january", "february", "march", "april", "may", "june")

    # Getting user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please choose a day of week:\n").lower()
    day_of_week = ["all", "monday", "tuesday", "wednesday", "thursday", "friday","saturday","sunday"]
    while (day not in day_of_week):
        day = input("Which day do you prefer?").lower()
        print('-'*40)

    return city, month, day

# Loaded data for specified city and filters by month and day.
def load_data(city, month, day):
  
    bikeshare = pd.read_csv(CITY_DATA[city])

# Converted the Start Time column to datetime
    bikeshare['Start Time'] = pd.to_datetime(bikeshare['Start Time'])

    # Extracted month and day of week from Start Time to create new columns

    bikeshare['month'] = bikeshare['Start Time'].dt.month

    bikeshare['day_of_week'] = bikeshare['Start Time'].dt.weekday_name

    # Filtered by month

    if month != 'all':
        # Used the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months.index(month) + 1

        # Filtered by month and created the new dataframe
    df = df[df['month'] == month]

    # Filtered by day of week
    if day != 'all':
        # Filtered by day of week and created the new dataframe
       df = df[df['day_of_week'] == day.title()]
    return df

# Displaying the most frequent times of travel
def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')


    start_time = time.time()

    # The most common month
    common_month = df['month'].mode()[0]
    print("The most common month is:", common_month)

    # The most common day of week
    day_week = df['day_of_week'].mode()[0]
    print("The most frequent day a week is:", day_week)

    # The most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common hour is:", popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# The most popular stations and trips.
def station_stats(df):
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # The most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most popular Start station is:", start_station)

    # The most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most common End Station is:", end_station)
    # The most frequent combination of start station and end station trip
    combination_start_end = df.groupby(['Start Station', 'End Station']).count()
    print("The most common combination Start and End Station trip is:", combination_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Displaying total and average trip duration
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time:", total_travel)

    # Mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Displaying Bikeshare users informations. "There is no data in gender and date of birth in Washington"
def user_stats(df):
   
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user:", user_types)

    # Counts of gender
    
    try:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:", gender_counts)
    except:
        print("There is no Gender informations in Washington:")

    # The earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print("Customer year of Birth:", earliest)
        recent = df['Birth Year'].max()
        print("Customer year of Birth:", recent)
        common = df['Birth Year'].mode()[0]
        print("Customer year of Birth:", common)
    except:
        print("There is no information in Washington:")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

