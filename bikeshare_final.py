import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTH_DATA = ['january','february','march',
            'april','may','june','all']

DAY = ['sunday','monday','tuesday','wednesday',
      'thursday','friday','saturday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Which city would you like to filter by? New York City, Chicago or Washington?\n").lower()
        if city not in (CITY_DATA.keys()):
            print("Sorry, I don't understand, please try again.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    
    while True:
        month = input("Which month would you like to filter by? January, "
                      "February, March, April, May,\nJune or type 'all' " 
                      "if you do not have any preference?\n").lower()
        if month not in MONTH_DATA:
            print("Sorry, I don't understand, please try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("Are you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, "
                    "Thursday,Friday, Saturday or type 'all' if you do not have any preference.\n").lower()
        if day not in DAY:
            
            print("Sorry, I don't understand, please try again.")
            continue
        else:
            break

    print('*' * 50)
    return (city, month, day)


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable

    if month != 'all':

            # use the index of the months list to get the corresponding int

       
        month = MONTH_DATA.index(month) + 1

        # filter by month to create the new dataframe

        df = df[df['month'] == month]

        # filter by day of week if applicable

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    "Displays statistics on the most frequent times of travel."

    print("The Most Frequent Times of Travel...")
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print ('Most Common Month:', popular_month)

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common Day:', popular_day)

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print('*' * 50)


def station_stats(df):
    "Displays statistics on the most popular stations and trip."

    print("The Most Popular Stations and Trip...")
    start_time = time.time()

    # TO DO: display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print ('Most Commonly Used Start Station:', Start_Station)

    # TO DO: display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly Used End Station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station'
            ]).count()
    print('\nMost Commonly Used Start Station and End Station Trip:'
           , Start_Station, ' & ', End_Station)
    print('*' * 50)


def trip_duration_stats(df):
    "Displays statistics on the total and average trip duration."

    print("Trip Duration...")
    start_time = time.time()

    # TO DO: display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time / 86400, ' Days')

    # TO DO: display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time / 60, ' Minutes')
    print('*' * 50)


def user_stats(df):
    "Displays statistics on bikeshare users."

    print("User Stats...")
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    # print(user_types)

    print('User Types:\n', user_types)

    # TO DO: Display counts of gender

    try:
        gender_types = df['Gender'].value_counts()
        print ('\nGender Types:\n', gender_types)
    except KeyError:
        print("Gender Types: No data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year:', Earliest_Year)
    except KeyError:
        print("Earliest Year: No data available for this month.")

    try:
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
        print("Most Recent Year: No data available for this month.")

    try:
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
        print("Most Common Year: No data available for this month.")
    print( '*' * 50)

def display_data(df):
    
    """Display contents of the CSV file requested by the user."""

    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5
            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break

def main():
    while True:
        (city, month, day) = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input("Would you like to restart? Enter yes or no.\n")
        if restart.lower() != 'yes':
            break


if __name__ == '__main__':
    main()


