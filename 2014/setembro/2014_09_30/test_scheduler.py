import unittest
from scheduler import optimize_schedule


class SchedulerTestCase(unittest.TestCase):

    def test_schedule_single_job(self):
        jobs = [(1, 3)]
        response = optimize_schedule(jobs)
        expected = [jobs]
        self.assertEqual(response, expected)

    def test_schedule_two_compatible_jobs(self):
        jobs = [(1, 3), (3, 5)]
        response = optimize_schedule(jobs)
        expected = [jobs]
        self.assertEqual(response, expected)

    def test_schedule_two_incompatible_jobs(self):
        jobs = [(1, 3), (2, 5)]
        response = optimize_schedule(jobs)
        expected = [[(1, 3)], [(2, 5)]]
        self.assertEqual(response, expected)

    def test_schedule_three_compatible_jobs(self):
        jobs = [(1, 3), (3, 5), (3, 4), (4, 5)]
        response = optimize_schedule(jobs)
        expected = [[(1, 3), (3, 4), (4, 5)]]
        self.assertEqual(response, expected)



unittest.main()
