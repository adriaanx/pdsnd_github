import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}


def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington)

    while True:
        print("Please choose one of those three cities: new york city, chicago, washington")
        cities = ['chicago', 'new york city', 'washington']
        city = input('Enter city: ').lower()
        if (city in cities):
            break
        else:
            print("Ups ... let's try this again")

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        print("Please choose the month you want to look at. Note data is only availale for the first six months.Type all, if you want to look at all the data availale")
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
        month = input('Enter a month: ').lower()
        if (month in months or month == "all"):
            break
        else:
            print("Ups ... let's try this again")

    while True:
        print("Please choose the day you want to look at. Type all, if you want to look at all the data availale")
        day = input('Enter day: ').lower()
        try:
            if (int(day) in range(1, 32)):
                break
        except:
            pass
        if (day == "all"):
            break
        print("Ups ... let's try this again")

    print('-'*40)

    return city, month, day


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

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day and hour of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month

    df['day'] = df['Start Time'].dt.day_name()

    df['hour'] = df['Start Time'].dt.hour

    if(month != 'all'):
        months = ['january', 'february', 'march', 'april', 'may, ''june']
        month = months.index(month) + 1
        df['month'] = month

    if(day != 'all'):
        df['day'] = day

    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
    most_common_month = int(df['month'].mode())
    most_common_month = months[most_common_month - 1]

    print("The most common month is {}".format(most_common_month))

    # display the most common month

    most_common_day = str(df['day'].mode())
    print("The most common day is {}".format(most_common_day))
    # display the most common day of week

    most_common_hour = str(df['hour'].mode())
    print("The most common hour is {} o'clock".format(most_common_hour))
    # display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_common_start_station = df['Start Station'].mode()
    print("The most common start station is {}".format(most_common_start_station))

    # display most commonly used end station

    most_common_end_station = df['End Station'].mode()
    print("The most common end station is {}".format(most_common_end_station))

    # display most frequent combination of start station and end station trip

    df['Start Stop Pair'] = df['Start Station'] + df['End Station']
    most_common_combination = df['Start Stop Pair'].mode()
    print("The most common Start Stop pair is {}".format(most_common_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    df['End Time'] = pd.to_datetime(df['End Time'])

    df['Travel Time'] = df['End Time'] - df['Start Time']

    total_travel_time = df['Travel Time'].sum()

    print("The total travel time is {}".format(total_travel_time))

    # display mean travel time

    mean_travel_time = df['Travel Time'].mean()
    print("The mean travel time is {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print("Now we show user types")

    print(df['User Type'].value_counts())

    # Display counts of gender

    print("Now we show gender counts")

    try:

        print(df['Gender'].value_counts())

    except:

        print("Unfortunately there is not gender data available for this city")

    # Display earliest, most recent, and most common year of birth

    try:

        earliest_year_of_birth = df['Birth Year'].min()
        most_recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].mode()
        print("The earliest year of birth is {}".format(earliest_year_of_birth))
        print("The most recent year of birth is {}".format(most_recent_year_of_birth))
        print("The most common year of birth is {}".format(most_common_year_of_birth))

    except:

        print("Unfortunately birth data is not available for your city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def show_lines(df):

    i = 0

    while True:
        illustration = input('\nDo you want to see 5 lines of raw data? Enter yes or no.\n').lower()
        options = ['yes', 'no']
        if (illustration in options):
            break
        else:
            print("Ups ... something went wrong. Let's try this again")

    while True:
        if (illustration == "no"):
            break
        elif (illustration == "yes"):
            print(df.iloc[i:(i+5)])
            i += 5
            while True:
                illustration = input('\nDo you want to see 5 more lines of raw data? Enter yes or no.\n').lower()
                options = ['yes', 'no']
                if (illustration in options):
                    break
                else:
                    print("Ups ... something went wrong. Let's try this again")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_lines(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
