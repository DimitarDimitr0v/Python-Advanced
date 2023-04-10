from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("Rampage", 2020, 5.0)
        self.movie_1 = Movie("Die Hard", 1993, 4.9)

    def test_initialization(self):
        self.assertEqual("Rampage", self.movie.name)
        self.assertEqual(2020, self.movie.year)
        self.assertEqual(5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_name_setter_success(self):
        self.movie.name = "NewName"
        self.assertEqual("NewName", self.movie.name)

    def test_year_setter_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_year_setter_success(self):
        self.movie.year = 1887
        self.assertEqual(1887, self.movie.year)

    def test_add_actor_who_already_added_case(self):
        self.movie.actors = ["Dwayne Jonson"]

        result = self.movie.add_actor("Dwayne Jonson")
        self.assertEqual(f"Dwayne Jonson is already added in the list of actors!", result)

    def test_add_actor_who_is_added_for_first_time(self):
        self.movie.add_actor("Dwayne Jonson")

        self.assertEqual(["Dwayne Jonson"], self.movie.actors)

    def test_dunder_gt_between_ratings_case_first_movie_better(self):
        result = self.movie > self.movie_1
        self.assertEqual(f'"Rampage" is better than "Die Hard"', result)

    def test_dunder_gt_between_ratings_case_second_movie_better(self):
        result = self.movie_1 > self.movie
        self.assertEqual(f'"Rampage" is better than "Die Hard"', result)

    def test_dunder_repr_without_actors(self):
        self.assertEqual(f"Name: Rampage\n"
                         f"Year of Release: 2020\n"
                         f"Rating: 5.00\n"
                         f"Cast: ", self.movie.__repr__())


    def test_dunder_repr_with_actors(self):
        self.movie.actors = ["Dwayne Jonson, Emily Clarc"]

        self.assertEqual(f"Name: Rampage\n"
                         f"Year of Release: 2020\n"
                         f"Rating: 5.00\n"
                         f"Cast: Dwayne Jonson, Emily Clarc", self.movie.__repr__())


if __name__ == '__main__':
    main()
