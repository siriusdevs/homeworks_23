"""Module with an implemented TestDataInitialiser class."""
import json
import os
from collections.abc import Iterable
from contextlib import suppress
from datetime import datetime, timedelta
from typing import Generator, NoReturn

from hw2.src.bbtypes import TestDataItem, Users
from hw2.src.utils.common import validate_file_path


class TestDataGenerator(Iterable):
    """Represent iterable containing all the test data."""

    _number_of_files = 11
    _input_files_dir_path = 'hw2/test_files/input/'
    _output_files_dir_path = 'hw2/test_files/output/'
    _expected_files_dir_path = 'hw2/test_files/expected_output/'
    _last_modification_date_file_path = 'hw2/test_files/last_modification_date'

    def initialize_test_data(self) -> tuple[TestDataItem, ...]:
        """Initialise test_data and return it.

        Returns:
            The field containing the tuples of the following format: \
                ( \
                    input_file_path: path to file with users data, \
                    output_file_path: path file where we save necessary stats, \
                    expected_output_data: dict with correct statistics \
                )
        """
        self._modify_test_data()

        test_data = []
        for filename in self._generate_filenames():
            input_file_path = f'{self._input_files_dir_path}{filename}'
            output_file_path = f'{self._output_files_dir_path}{filename}'

            with open(f'{self._expected_files_dir_path}{filename}') as expected_output_file:
                expected_output_data = json.load(expected_output_file)

            test_data.append((input_file_path, output_file_path, expected_output_data))

        return tuple(test_data)

    def __iter__(self) -> Generator[tuple[TestDataItem, ...], None, None]:
        """Yield all the test items.

        Yields:
            All the test items.
        """
        yield from self.initialize_test_data()

    def _generate_filenames(self) -> Generator[str, None, None]:
        """Return a generator containing file names.

        Yields:
            The name for the file from 1.json to 10.json
        """
        yield from (f'{file_num}.json' for file_num in range(1, self._number_of_files + 1))

    def _modify_test_data(self) -> NoReturn:
        """Modify last_login of all users according to \
        the current date so that the tests work with the already existing expected_data."""
        if not os.path.exists(self._last_modification_date_file_path):
            self._update_last_modification_date()
            return

        # load the last modification date and determine the difference with the current date
        with open(self._last_modification_date_file_path, 'r') as last_modification_date_file:
            last_modification_date = datetime.fromisoformat(
                last_modification_date_file.read(),
            )
        date_diff: timedelta = datetime.now() - last_modification_date

        for filename in self._generate_filenames():
            # skip files with invalid path and invalid JSON syntax
            with suppress(json.JSONDecodeError, FileNotFoundError):
                input_file_path = f'{self._input_files_dir_path}{filename}'
                validate_file_path(input_file_path)

                with open(input_file_path, 'r') as input_file:
                    # skip files with invalid JSON syntax
                    input_data = json.load(input_file)

                updated_data: Users = self._update_input_data(input_data, date_diff)
                self._save_updated_data(input_file_path, updated_data)

        # update last_modification_date
        self._update_last_modification_date()

    def _update_last_modification_date(self) -> NoReturn:
        """Update the date in the last_modification_date \
        file to the current date."""
        with open(self._last_modification_date_file_path, 'w') as last_modification_date_file:
            last_modification_date_file.write(datetime.now().strftime('%Y-%m-%d'))

    @staticmethod
    def _update_input_data(input_user_data: Users, date_diff: timedelta) -> Users:
        """Update last_login field in received input_user_data \
        and return it.

        Args:
            input_user_data (Users): user data we need to update.
            date_diff (timedelta): the difference between current date and last_modification_date.

        Returns:
            An updated input_user_data.
        """
        for user in input_user_data.values():
            # skip files with invalid user model
            try:
                old_last_login_date = datetime.fromisoformat(user['last_login'])
            except KeyError:
                continue
            user['last_login'] = (old_last_login_date + date_diff).strftime('%Y-%m-%d')
        return input_user_data

    @staticmethod
    def _save_updated_data(input_file_path: str, updated_data: Users) -> NoReturn:
        """Write an updated data to input_file.

        Args:
            input_file_path (str): path to the input file that we need to update.
            updated_data (Users): data that we need to write to input file.
        """
        with open(input_file_path, 'w') as input_file:
            json.dump(updated_data, input_file, indent=4, ensure_ascii=False)
