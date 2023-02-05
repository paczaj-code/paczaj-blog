from django.test import TestCase
from blog.models import Post
from category.models import Category
from practise.models import Practice, Exercise
# from practice.models import Practice, Exercise
from django.core.management import call_command


class PracticeTest(TestCase):
    """Test practise model"""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures.json', verbosity=0)

    def test_inserted_fixtures(self):
        self.assertEqual(Practice.objects.get(id=1).title, 'Practise 1')
        self.assertEqual(Practice.objects.get(id=1).slug, 'practise-1')
        self.assertEqual(Practice.objects.get(id=1).slug, 'practise-1')
        self.assertEqual(Practice.objects.get(
            id=1).category, Category.objects.get(id=1))
        self.assertEqual(Practice.objects.get(
            id=1).description, 'Practise 1 decription')
        self.assertEqual(Practice.objects.get(id=1).related_posts.count(), 2)

    def test_create_parctise_withot_title_raises_error(self):
        with self.assertRaises(Exception):
            Practise.objects.create(
                title=None)

    def test_create_parctise_withot_category_raises_error(self):
        with self.assertRaises(Exception):
            Practise.objects.create(
                title='Some', category=None)

    def test_create_parctise_withot_description_raises_error(self):
        with self.assertRaises(Exception):
            Practise.objects.create(
                title='Some', category=Category.objects.get(id=2), description=None)

    def test_create_practise(self):
        Practice.objects.create(
            title="New practise", category=Category.objects.get(id=2), description="New description",
            is_published=False
        )
        self.assertEqual(Practice.objects.count(), 3)
        self.assertEqual(Practice.objects.last().title, 'New practise')
        self.assertEqual(Practice.objects.last().slug, 'new-practise')
        self.assertEqual(Practice.objects.last().is_published, False)
        self.assertEqual(Practice.objects.last().description,
                         'New description')

    def test_update_practice(self):
        practice = Practice.objects.get(id=2)
        practice.title = 'New title'
        practice.is_published = True
        practice.category = Category.objects.get(id=1)
        practice.related_posts.add(Post.objects.get(id=1))
        practice.related_posts.remove(Post.objects.get(id=2))
        # practice.related_posts.remove(Post.objects.get(id=3))
        practice.save()

        self.assertEqual(Practice.objects.get(id=2).title, 'New title')
        self.assertEqual(Practice.objects.get(id=2).slug, 'new-title')
        self.assertEqual(Practice.objects.get(id=2).is_published, True)
        self.assertEqual(Practice.objects.get(id=2).category,
                         Category.objects.get(id=1))
        self.assertEqual(Practice.objects.get(id=2).related_posts.count(), 1)
        self.assertEqual(Practice.objects.get(
            id=2).related_posts.first(), Post.objects.get(id=1))

    def test_delete_practise(self):
        Practice.objects.get(id=1).delete()
        self.assertEqual(Practice.objects.count(), 1)


class ExerciseTest(TestCase):
    """Test exersice model"""
    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'fixtures/fixtures.json', verbosity=0)

    def test_inserted_fixtures(self):
        self.assertEqual(Exercise.objects.count(), 2)
        self.assertEqual(Exercise.objects.get(id=1).number, 1)
        self.assertEqual(Exercise.objects.get(
            id=1).practise, Practice.objects.get(id=1))
        self.assertEqual(Exercise.objects.get(id=1).difficulty, 'E')
        self.assertEqual(Exercise.objects.get(id=1).exercise, 'Exersise 1')
        self.assertEqual(Exercise.objects.get(id=1).solution, 'Solution 1')
        self.assertEqual(Exercise.objects.get(id=1).is_published, True)
        self.assertEqual(Exercise.objects.get(id=2).is_published, False)

    def test_create_exercise_without_practice_raises_error(self):
        with self.assertRaises(Exception):
            Exercise.objects.create(
                practise=None)

    def test_create_exercise_without_difficulty_raises_error(self):
        with self.assertRaises(Exception):
            Exercise.objects.create(
                practise=Practice.objects.get(id=1), difficulty=None)

    def test_create_exercise_without_exercise_raises_error(self):
        with self.assertRaises(Exception):
            Exercise.objects.create(
                practise=Practice.objects.get(id=1), difficulty="M",
                exercise=None
            )

    def test_create_exercise_without_solution_raises_error(self):
        with self.assertRaises(Exception):
            Exercise.objects.create(
                practise=Practice.objects.get(id=1), difficulty="M",
                exercise='exersice', solution=None
            )

    def test_create_exercise(self):
        Exercise.objects.create(
            number=4,
            practise=Practice.objects.get(id=1), difficulty="M",
            exercise='exersice', solution='solution'
        )
        self.assertEqual(Exercise.objects.count(), 3)
        self.assertEqual(Exercise.objects.last().number, 3)
        self.assertEqual(Exercise.objects.last().exercise, 'exersice')
        self.assertEqual(Exercise.objects.last().solution, 'solution')
        self.assertEqual(Exercise.objects.last().difficulty, 'M')
        self.assertEqual(Exercise.objects.last().is_published, True)
        self.assertEqual(Exercise.objects.last().practise,
                         Practice.objects.get(id=1))

    def test_update_exercise(self):
        exercise = Exercise.objects.get(id=2)
        exercise.number = 100
        exercise.exercise = 'New exercise'
        exercise.solution = 'New solution'
        exercise.is_published = True
        exercise.save()

        self.assertEqual(Exercise.objects.get(id=2).number, 100)
        self.assertEqual(Exercise.objects.get(id=2).exercise, 'New exercise')
        self.assertEqual(Exercise.objects.get(id=2).solution, 'New solution')
        self.assertEqual(Exercise.objects.get(id=2).is_published, True)

    def test_delete_exercise(self):
        Exercise.objects.get(id=1).delete()
        self.assertEqual(Exercise.objects.count(), 1)
