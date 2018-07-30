# @Author: daibin
# @Date:   2018-05-17T19:07:12+08:00
# @Last modified by:   daibin
# @Last modified time: 2018-05-28T11:36:03+08:00

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': './data/chicago.csv',
              'new york': './data/new_york_city.csv',
              'washington': './data/washington.csv' }
INPUT_LIST = {
    'city': ['Chicago', 'New York', 'Washington'],
    'month': ['all', 'January', 'February', 'March', 'April', 'May', 'June'],
    'week': ['all', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
}

def is_equal(key, list):
    equal = False
    for item in list:
        if key.lower() == item.lower():
            equal = True
    return equal

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = month = day = ''

    while not is_equal(city, INPUT_LIST['city']):
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while not is_equal(month, INPUT_LIST['month']):
        month = input('\nWhich month? all, January, February, March, April, May, June?\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while not is_equal(day, INPUT_LIST['week']):
        day = input('\nWhich day? all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?\n')

    print('-'*40)
    print()
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas Data\Frame containing city data filtered by month and day
    """
    print('Loading Data...')
    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Common Month => ', popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_week = df['day_of_week'].mode()[0]
    print('Most Common Day Of Week => ', popular_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour => ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_types = df['Start Station'].head()[0]
    print('most commonly used start station is => '.title(), start_types)

    # TO DO: display most commonly used end station
    end_types = df['End Station'].head()[0]
    print('most commonly used end station is => '.title(), end_types)

    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station trip is => '.title(),
        start_types,
        ' -> ',
        end_types)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

    # TO DO: display total travel time
    trip_type = df['Trip Duration'].sum()
    print('total travel time => '.title(), trip_type)

    # TO DO: display mean travel time
    mean_type = df['Trip Duration'].mean()
    print('mean travel time => '.title(), mean_type)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types => '.title(), user_types)


    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    print('counts of gender => \n'.title(), gender_types)


    # TO DO: Display earliest, most recent, and most common year of birth
    sort_types = df.dropna().sort_values(['Birth Year'], ascending=True)

    earliest_birth_types = int(sort_types.head(1)['Birth Year'])
    print('earliest year of birth =>'.title(), earliest_birth_types)

    recent_birth_types = int(sort_types.tail(1)['Birth Year'])
    print('most recent year of birth =>'.title(), recent_birth_types)


    common_birth_types = int(df['Birth Year'].value_counts().index[0])
    print('most common year of birth => '.title(), common_birth_types)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()


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
