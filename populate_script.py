import names
import random
import os
import django
import pickle
import argparse
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
discipline_details = {"Computer Science": {"supervisors":
                                              ["Dr. R Gururaj",
                                               "Prof. NL Bhanumurthy",
                                               "Prof. Aruna Malapati",
                                               "Prof. Tathagata Ray"],
                                           "research_area":
                                                   ["Machine Learning",
                                                    "Artificial Intelligence",
                                                    "Origami Folding"
                                                    " Algorithms"],
                                           "courses": {
                                                 "CS-F211": "Information"
                                                            " Retrieval",
                                                 "CS-F212": "Advanced Computer"
                                                            " Networks",
                                                 "CS-F213": "Advanced Computer"
                                                            " Architecture",
                                                 "CS-F214": "Computational"
                                                            " Geometry",
                                                 "CS-F215": "Design and"
                                                            " Analysis of"
                                                            "Algorithms"
                                               }},
                      "EEE": {"supervisors": ["Prof. Chetan Kumar",
                                              "Prof. Sanket Goyal"],
                              "research_area": ["Digital Signal Processing",
                                                "Embedded Systems",
                                                "Microprocessors"],
                              "courses": {
                                    "EEE-F211": "Power Electronics",
                                    "EEE-F212": "Digital Image Processing",
                                    "EEE-F213": "Advanced Microprocessors",
                                    "EEE-F214": "Analog Electronics"
                                  }},
                      "Pharmacy": {"supervisors":
                                   ["Dr. Sajeli Begum",
                                    "Prof. P.Yogeeswari"],
                                   "research_area": ["Pharmaceutical"
                                                     " Cell Biology",
                                                     "Medicines Management",
                                                     "Drug Delivery"],
                                   "courses": {"PHA-F211": "Dispensing"
                                                           " Pharmacy",
                                               "PHA-F212": "Pharmaceutical"
                                                           "Chemistry",
                                               "PHA-F213": "Pharmacology",
                                               "PHA-F214": "Medicinal"
                                                           " Chemistry"}},

                      "Humanities and"
                      " Social Sciences": {"supervisors":
                                               ["Dr. M G Prasuna",
                                                "Prof. Maya Vinai"],
                                               "research_area":
                                               ["Critical Analysis"
                                                " of Literature and Cinema",
                                                "Post Colonial Literature"],
                                               "courses": {
                                                 "HSS-F211": "Linguistics",
                                                 "HSS-F212": "Heritage of"
                                                             " India",
                                                 "HSS-F213": "Advanced Business"
                                                             "Communication",
                                                 "HSS-F214": "Effective Public"
                                                             "Speaking"
                                               }},
                      "Biological Sciences": {"supervisors":
                                               ["Dr. Vidya Rajesh",
                                                   "Dr. Sankar Ganesh"],
                                                   "research_area":
                                              ["Genetics",
                                                  "Computational Biology"],
                                              "courses": {
                                                    "BIO-F211": "Advanced Cell"
                                                                " and Molecular"
                                                                " Biology",
                                                    "BIO-F212": "Plant"
                                                                " Biotechnology",
                                                    "BIO-F213": "Introduction to"
                                                                " Bio"
                                                                "informatics",
                                                    "BIO-F214": "Advanced and "
                                                                "Applied"
                                                                " Microbiology"
                                                  }}}
def add_phd_scholars_thesis():
  id_number_template = "2018PHXF00"
  fellowship_types = ["No Fellowship", "Own Fellowship",
                      "Project Fellow", "Institute Fellowship"]
  for i in range(1, 51):
    if i < 10:
      id_str = "0{id}H".format(id=i)
    else:
      id_str = "{id}H".format(id=i)
    scholar_id_number = id_number_template + id_str
    scholar_department = random.choice(discipline_details.keys())
    scholar_supervisor = random.choice(discipline_details
                                       [scholar_department]['supervisors'])
    scholar_research_area = random.choice(discipline_details
                                          [scholar_department]['research_area'])
    scholar_name = names.get_full_name()
    scholar_fellowship_type = random.choice(fellowship_types)
    try:
      _ = PhDScholar.objects.get(id_number=scholar_id_number)
    except PhDScholar.DoesNotExist:
      phd_scholar = PhDScholar(id_number=scholar_id_number,
                               name=scholar_name,
                               department=scholar_department,
                               fellowship_type=scholar_fellowship_type)
      phd_scholar.save()
      phd_thesis = PhDThesis(id_number=phd_scholar,
                             supervisor=scholar_supervisor,
                             research_area=scholar_research_area)
      phd_thesis.save()


def update_department_course_pickle():
  with open("dept_course_pickle", "r+") as f:
    try:
      dept_to_course = pickle.load(f)
    except EOFError:
      print("Updating pickle file for the first time.")
      dept_to_course = dict()
      first_dept_to_course_dict = update_department_course_dict(dept_to_course)
      print first_dept_to_course_dict
      pickle.dump(first_dept_to_course_dict, f)
      return
  with open("dept_course_pickle", "w+") as f:
    updated_dept_to_course = update_department_course_dict(dept_to_course)
    print updated_dept_to_course
    pickle.dump(updated_dept_to_course, f)


def update_department_course_dict(department_to_course_dict):
  department_to_course_alias = {
    "Computer Science": "CS",
    "EEE": "EEE",
    "Pharmacy": "PHA",
    "Biological Sciences":"BIO",
    "Humanities and Social Sciences": "HSS"
  }
  phd_courses = PhDCourses.objects.all()
  for course in phd_courses:
    for dept, alias in department_to_course_alias.iteritems():
      if not department_to_course_dict.get(dept):
        department_to_course_dict[dept] = list()
      if alias in course.course_id:
        x = set(department_to_course_dict[dept])
        x.add(course)
        department_to_course_dict[dept] = list(x)
  return department_to_course_dict

def add_scholar_courses():
  with open("dept_course_pickle", "r+") as f:
    dept_to_course_list = pickle.load(f)
  phd_scholars = PhDScholar.objects.all()
  for scholar in phd_scholars:
    scholar_department = scholar.department
    random_courses = random.sample(dept_to_course_list[scholar_department], 2)
    for course in random_courses:
      try:
        _ = PhDScholarCourses.objects.get(id_number=scholar,
                                          course_id=course)
      except PhDScholarCourses.DoesNotExist:
        phd_scholar_course = PhDScholarCourses(id_number=scholar, course_id=course)
        phd_scholar_course.save()


def add_courses():
  for discipline in discipline_details:
    for course_id,\
          course_name in discipline_details[discipline]["courses"].iteritems():
            try:
              _ = PhDCourses.objects.get(course_id=course_id)
            except PhDCourses.DoesNotExist:
              phd_course = PhDCourses(course_id=course_id,
                                      course_name=course_name, credits=3)
              phd_course.save()


if __name__ == '__main__':
  os.environ['DJANGO_SETTINGS_MODULE'] = 'phd_application.settings'
  django.setup()
  from phd_info_mgmt_system.models import PhDScholar, PhDThesis, PhDCourses, PhDScholarCourses
  parser = argparse.ArgumentParser()
  parser.add_argument('--update_pickle', action='store_true', default=False)
  args = parser.parse_args()
  logging.info("Adding 50 dummy PhD Scholars"
               " along with their thesis information.")
  add_phd_scholars_thesis()
  logging.info("Adding courses to the database.")
  add_courses()
  if args.update_pickle:
    logging.info("Updating the pickle to"
                 " add newly added courses to the data structure.")
    update_department_course_pickle()
  logging.info("Assigning random courses"
               " to the scholars added, according to the scholar discipline.")
  add_scholar_courses()
