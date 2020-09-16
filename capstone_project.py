import time
import pandas as pd
import numpy as np
import statistics

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print('Hello! Lets explore some bikeshare data!')
        print('Would you like to see data for Chicago, New York or Washington')
        city = input().lower()

        if city not in CITY_DATA.keys():
            print('Please, Check your input and restart the program')

    print(f'{city.title()}')

    # get user input for month (all, january, february, ... , june)
    all_months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in all_months.keys():
        print('Welcome back!')
        print('Would you like to see data by month?\nIf yes enter a month of your Choice')
        month = input().lower()

        if month not in all_months.keys():
            print('Please, Check your input and restart the program')

    print(f'{month.title()}')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    all_days = ['all', 'M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
    day = ''
    while day not in all_days:
        print('Would you like to see data by day?\nIf yes enter a day of your Choice')
        day = input().lower()

        if day not in all_days:
            print('Please, Check your input and restart the program')

    print(f'{day.title()}')

    print(f'You are about to view the following data! {city.upper()}, {month.upper()}, {day.upper()}')

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
    print('Just one moment... Loading the data')
    df = pd.read_csv[CITY_DATA[city]]
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(f'The most popular month: {common_month}')
    # display the most common day of week
    common_day = df['day'].mode()[0]
    print(f'The most common day is: {common_day}')
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f'The most popular start hour: {common_hour}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    start_station = df['Start Station'].mode()[0]
    print(f'The most common Start station is: {start_station}')
    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f'The most common End station is: {end_station}')
    # display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'] + 'to' + df['End Station']
    start_to_end = df['Start to End'].mode()[0]
    print(f'The combination of start to end station trip is: {start_to_end}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(sum(df['Trip Duration']))

    # display mean travel time
    print(statistics.mean(df['Trip Duration']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f'Counts of user type are: {user_type}')

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print(f'Gender of the Users: {gender}')

    # Display earliest, most recent, and most common year of birth
    earliest = max(df['Birth Year'])
    recent = min(df['Birth Year'])
    common = int(df['Birth Year'].mode()[0])
    print(f'The earliest year of birth: {earliest}\nThe most recent year of birth: {recent}\nThe most common year of birth: {common}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()




























