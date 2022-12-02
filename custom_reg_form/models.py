from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """

    LIKERT_CHOICES = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five')
    )

    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
        ('na', 'No answer')
    )

    LIKERT_CHOICES_W_DUNNO_5 = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
        ('6', '-')
    )

    LIKERT_CHOICES_W_DUNNO = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
        ('6', 'Six'),
        ('7', 'Seven'),
        ('8', '-')
    )

    GRADE_CHOICES = (
        ('1', '1.0'),
        ('2', '1.3'),
        ('3', '1.7'),
        ('4', '2.0'),
        ('5', '2.3'),
        ('6', '2.7'),
        ('7', '3.0'),
        ('8', '3.3'),
        ('9', '3.7'),
        ('10', '4.0'),
        ('11', '5.0'),
        ('12', 'No answer')
    )

    STUDY_PROGRAMM_CHOICES = (
        ('Information Systems (Wirtschaftsinformatik)', 'Information Systems (Wirtschaftsinformatik)'),
        ('International Information Systems Management', 'International Information Systems Management'),
        ('Business Administration', 'Business Administration & Management (BWL)'),
        ('International Business Administration', 'International Business Administration & Management (IBWL)'),
        ('Applied Computer Science', 'Applied Computer Science'),
        ('Computing in the Humanities', 'Computing in the Humanities'),
        ('International Software Systems Science', 'International Software Systems Science'),
        ('Survey Statistics', 'Survey Statistics'),
        ('Other', 'Other'),
        ('No answer', 'No answer'),
    )

    STUDY_LEVEL_CHOICES = (
        ("1. to 2.", "1. to 2."),
        ("3. to 4.", "3. to 4."),
        ("5. to 6.", "5. to 6."),
        ("7. to 8.", "7. to 8."),
        ("9. to 10.", "9. to 10."),
        (">10.", ">10."),
        ('No answer', 'No answer')
    )

    NO_YES = (
        ("Yes", "Yes"),
        ("No", "No")
    )
    LANGUAGES_CHOICES_REDUCED = (
        ("DE", "German"),
        ("EN", "English"),
        ("FR", "French"),
        ("ZH", "Chinese"),
        ("HR", "Croation"),
        ("CS", "Czech"),
        ("DA", "Danish"),
        ("NL", "Dutch"),
        ("FI", "Finnish"),
        ("IW", "Hebrew"),
        ("HI", "Hindi"),
        ("GA", "Irish"),
        ("IT", "Italian"),
        ("JA", "Japanese"),
        ("KO", "Korean"),
        ("NO", "Norwegian"),
        ("PL", "Polish"),
        ("PT", "Portuguese"),
        ("RU", "Russian"),
        ("SR", "Serbian"),
        ("ES", "Spanish"),
        ("SV", "Swedish"),
        ("TR", "Turkish"),
        ("UK", "Ukranian"),
        ("UR", "Urdu"),
        ("Other", "Other")
    )

    user = models.OneToOneField(USER_MODEL, null=True, related_name='user+', on_delete=models.CASCADE)

    consent = models.BooleanField(
        verbose_name="I agree that data of my learning behavior may be used to improve the EESYS courses.",
        default=1,
    )
    study_programme = models.CharField(verbose_name="Please enter your study program.", choices=STUDY_PROGRAMM_CHOICES,
                                       max_length=255)

    enhanced_gender = models.CharField(verbose_name="Please enter your gender.", choices=GENDER_CHOICES, max_length=255)

    current_semester_of_study = models.CharField(verbose_name="Please enter your current semester of study.",
                                                 choices=STUDY_LEVEL_CHOICES, max_length=15)

    part_time_student = models.CharField(verbose_name="Are you a part-time student?", choices=NO_YES, max_length=15)

    bachelor_level_statistics = models.CharField(
        verbose_name="Have you taken a bachelor's-level statistics or data analytics course before?", choices=NO_YES,
        max_length=100)
    master_level_statistics = models.CharField(
        verbose_name="Have you taken a master's-level statistics or data analytics course before?", choices=NO_YES,
        max_length=100)

    familiar_with_R = models.CharField(verbose_name="Are you familiar with the programming language R?", choices=NO_YES,
                                       max_length=50)

    # Likert Please rate your level of agreement with the following statements:
    importance_DAEI = models.CharField(verbose_name="Data analytics is important for my future career.",
                                       choices=LIKERT_CHOICES, max_length=100)
    motivation_DAEI = models.CharField(
        verbose_name="It is important to me to achieve a very good grade (between 1.0 and 1.7) in the IITP course.",
        choices=LIKERT_CHOICES, max_length=100)

    # Likert
    procrastinate = models.CharField(verbose_name="How often do you procrastinate?", choices=LIKERT_CHOICES,
                                     max_length=80)

    # Likert Do you often ...
    measure_self_set_goals = models.CharField(
        verbose_name="Do you often measure your performance against self-set goals?", choices=LIKERT_CHOICES,
        max_length=100)
    measure_around_you = models.CharField(
        verbose_name="Do you often measure your performance against the performance of people around you?",
        choices=LIKERT_CHOICES, max_length=100)

    more_time_on_course = models.CharField(max_length=30,
                                           verbose_name="What do you think? How many out of 100 students will spend more time on the IITP course than you do?")

    course_how_many_students_studying = models.CharField(max_length=30,
                                                         verbose_name="What do you think? How many out of 100 students will spend more time studying this semester than you do?")

    list_zp1 = models.CharField(verbose_name="ZP1", choices=LIKERT_CHOICES, max_length=80)
    list_zp2 = models.CharField(verbose_name="ZP2", choices=LIKERT_CHOICES, max_length=80)
    list_zp3 = models.CharField(verbose_name="ZP3", choices=LIKERT_CHOICES, max_length=80)

    list_kon1 = models.CharField(verbose_name="Kon1", choices=LIKERT_CHOICES, max_length=80)
    list_kon2 = models.CharField(verbose_name="Kon2", choices=LIKERT_CHOICES, max_length=80)
    list_kon3 = models.CharField(verbose_name="Kon3", choices=LIKERT_CHOICES, max_length=80)

    list_reg1 = models.CharField(verbose_name="Reg1", choices=LIKERT_CHOICES, max_length=80)
    list_reg2 = models.CharField(verbose_name="Reg2", choices=LIKERT_CHOICES, max_length=80)
    list_reg3 = models.CharField(verbose_name="Reg3", choices=LIKERT_CHOICES, max_length=80)

    list_lang = models.CharField(verbose_name="What is your native language?", choices=LANGUAGES_CHOICES_REDUCED,
                                 max_length=120)

    # notenziel self-assigned goals (Locke & Latham, 1990)/ grade expactation (Lane & Gibbons, 2007)
    # open scale
    scale_gradegoal1 = models.CharField(choices=GRADE_CHOICES, max_length=80,
                                        verbose_name="What is the minimum (i.e. the least you would be satisfied with) grade goal for the final exam?")
    scale_gradegoal2 = models.CharField(choices=GRADE_CHOICES, max_length=80,
                                        verbose_name="Which grade do you aim for in the final exam?")
    your_age = models.CharField(max_length=30, verbose_name="Please enter your age.")

    # mslq pintrich 1991
    # likert7
    scale_efficacy1 = models.CharField(verbose_name="efficacy1", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_efficacy2 = models.CharField(verbose_name="efficacy2", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_efficacy3 = models.CharField(verbose_name="efficacy3", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_efficacy4 = models.CharField(verbose_name="efficacy4", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_efficacy5 = models.CharField(verbose_name="efficacy5", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_efficacy6 = models.CharField(verbose_name="efficacy6", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_efficacy7 = models.CharField(verbose_name="efficacy7", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_efficacy8 = models.CharField(verbose_name="efficacy8", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)

    # mslq pintrich 1991
    # likert7
    scale_meta_cog1 = models.CharField(verbose_name="meta_cog1", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog2 = models.CharField(verbose_name="meta_cog2", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog3 = models.CharField(verbose_name="meta_cog3", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog4 = models.CharField(verbose_name="meta_cog4", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog5 = models.CharField(verbose_name="meta_cog5", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog6 = models.CharField(verbose_name="meta_cog6", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog7 = models.CharField(verbose_name="meta_cog7", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog8 = models.CharField(verbose_name="meta_cog8", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog9 = models.CharField(verbose_name="meta_cog9", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog10 = models.CharField(verbose_name="meta_cog10", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog11 = models.CharField(verbose_name="meta_cog11", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_meta_cog12 = models.CharField(verbose_name="meta_cog12", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)

    # mslq pintrich 1991
    # likert7
    scale_mnmgt_int1 = models.CharField(verbose_name="mnmgt_int1", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int2 = models.CharField(verbose_name="mnmgt_int2", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int3 = models.CharField(verbose_name="mnmgt_int3", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int4 = models.CharField(verbose_name="mnmgt_int4", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int5 = models.CharField(verbose_name="mnmgt_int5", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int6 = models.CharField(verbose_name="mnmgt_int6", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int7 = models.CharField(verbose_name="mnmgt_int7", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int8 = models.CharField(verbose_name="mnmgt_int8", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int9 = models.CharField(verbose_name="mnmgt_int9", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int10 = models.CharField(verbose_name="mnmgt_int10", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int11 = models.CharField(verbose_name="mnmgt_int11", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_mnmgt_int12 = models.CharField(verbose_name="mnmgt_int12", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)

    # mslq pintrich 1991
    # likert7
    scale_cog1 = models.CharField(verbose_name="cog1", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_cog2 = models.CharField(verbose_name="cog2", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_cog3 = models.CharField(verbose_name="cog3", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_cog4 = models.CharField(verbose_name="cog4", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_cog5 = models.CharField(verbose_name="cog5", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_cog6 = models.CharField(verbose_name="cog6", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_cog7 = models.CharField(verbose_name="cog7", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_cog8 = models.CharField(verbose_name="cog8", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)

    # APS-S (Yockey, 2016 in Anlehnung an McCloskey, 2011)
    scale_proc1 = models.CharField(verbose_name="proc1", choices=LIKERT_CHOICES_W_DUNNO_5, max_length=80)
    scale_proc2 = models.CharField(verbose_name="proc2", choices=LIKERT_CHOICES_W_DUNNO_5, max_length=80)
    scale_proc3 = models.CharField(verbose_name="proc3", choices=LIKERT_CHOICES_W_DUNNO_5, max_length=80)
    scale_proc4 = models.CharField(verbose_name="proc4", choices=LIKERT_CHOICES_W_DUNNO_5, max_length=80)
    scale_proc5 = models.CharField(verbose_name="proc5", choices=LIKERT_CHOICES_W_DUNNO_5, max_length=80)

    # big five
    # likert5
    scale_big5_1 = models.CharField(verbose_name="big5_1", choices=LIKERT_CHOICES_W_DUNNO_5, max_length=80)
    scale_big5_2 = models.CharField(verbose_name="big5_2", choices=LIKERT_CHOICES_W_DUNNO_5, max_length=80)

    # mslq pruefungsangst 1991
    # likert7
    scale_anxiety1 = models.CharField(verbose_name="anxiety1", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_anxiety2 = models.CharField(verbose_name="anxiety2", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_anxiety3 = models.CharField(verbose_name="anxiety3", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_anxiety4 = models.CharField(verbose_name="anxiety4", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)
    scale_anxiety5 = models.CharField(verbose_name="anxiety5", choices=LIKERT_CHOICES_W_DUNNO, max_length=80)


def __str__(self):
    result = '{0.user} {0.nationality} {0.age} {0.phone_number}'
    return result.format(self)  #
