from .models import ExtraInfo
from django.forms import ModelForm


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """

    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)

        self.fields["consent"].required = True
        self.fields["consent"].initial = 1
        self.fields["consent"].blank = True

        self.fields["study_programme"].required = True
        self.fields["study_programme"].error_messages = {
            "required": u"Please tell us your study program.",
            "invalid": u"The study program is not valid.",
        }

        self.fields["enhanced_gender"].error_messages = {
            "required": u"Please enter your gender.",
            "invalid": u"The gender is not valid.",
        }
        self.fields["your_age"].required = False

        self.fields["your_age"].error_messages = {
            "required": u"Please tell us about your age.",
            "invalid": u"The age is not valid.",
        }

        self.fields["current_semester_of_study"].required = True
        self.fields["current_semester_of_study"].error_messages = {
            "required": u"Please tell us your current semester of study.",
            "invalid": u"The entered semester of study is not valid.",
        }

        self.fields["part_time_student"].required = True
        self.fields["part_time_student"].error_messages = {
            "required": u"Please tell us whether you are a part-time student.",
            "invalid": u"Your answer is not valid.",
        }

        self.fields["bachelor_level_statistics"].required = False
        self.fields["bachelor_level_statistics"].error_messages = {
            "required": u"Please tell us whether you have taken a bachelor's-level project management course before.",
            "invalid": u"Your answer is not valid.",
        }

        self.fields["master_level_statistics"].required = False
        self.fields["master_level_statistics"].error_messages = {
            "required": u"Please tell us whether you have taken a master's-level statistics or data analytics course before.",
            "invalid": u"Your answer is not valid.",
        }

        self.fields["familiar_with_R"].required = False
        self.fields["familiar_with_R"].error_messages = {
            "required": u"Please tell us whether you are familiar with the programming language R.",
            "invalid": u"Your answer is not valid.",
        }

        self.fields["importance_DAEI"].required = False
        self.fields["importance_DAEI"].error_messages = {
            "required": u"Please let us know how important you think data analytics is for your future career.",
            "invalid": u"Your answer is not valid.",
        }

        self.fields["motivation_DAEI"].required = False
        self.fields["motivation_DAEI"].error_messages = {
            "required": u"Please let us know how important it is for you to achieve a very good grade (between 1.0 and 1.7) in IITP.",
            "invalid": u"Your answer is not valid.",
        }

        self.fields["measure_self_set_goals"].required = False
        self.fields["measure_self_set_goals"].error_messages = {
            "required": u"Please let us know how: Do you often measure your performance against self-set goals?",
            "invalid": u"Your answer is not valid.",
        }

        self.fields["measure_around_you"].required = False
        self.fields["measure_around_you"].error_messages = {
            "required": u"Please let us know how: Do you often measure your performance against the performance of people around you?",
            "invalid": u"Your answer is not valid.",
        }

        self.fields["procrastinate"].required = False
        self.fields["procrastinate"].error_messages = {
            "required": u"Please let us know how often you procrastinate.",
            "invalid": u"Your answer is not valid.",
        }

        self.fields["list_zp1"].required = False
        self.fields["list_zp1"].error_messages = {
            "required": u"Please tell us your study program.",
            "invalid": u"The study program is not valid.",
        }
        self.fields["list_zp2"].required = False
        self.fields["list_zp3"].required = False
        self.fields["list_kon1"].required = False
        self.fields["list_kon2"].required = False
        self.fields["list_kon3"].required = False
        self.fields["list_reg1"].required = False
        self.fields["list_reg2"].required = False
        self.fields["list_reg3"].required = False
        self.fields["list_lang"].required = False

        self.fields["scale_gradegoal1"].required = True
        self.fields["scale_gradegoal2"].required = True

        self.fields["scale_gradegoal1"].error_messages = {
            "required": u"Missing answer regarding goal grades.",
        }
        self.fields["scale_gradegoal2"].error_messages = {
            "required": u"Missing answer regarding goal grades.",
        }

        self.fields["scale_efficacy1"].required = True
        self.fields["scale_efficacy2"].required = True
        self.fields["scale_efficacy3"].required = True
        self.fields["scale_efficacy4"].required = True
        self.fields["scale_efficacy5"].required = True
        self.fields["scale_efficacy6"].required = True
        self.fields["scale_efficacy7"].required = True
        self.fields["scale_efficacy8"].required = True

        self.fields["scale_efficacy1"].error_messages = {
            "required": u"Please answer the question: I believe I will receive an excellent grade in this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_efficacy2"].error_messages = {
            "required": u"Please answer the question: I'm certain I can understand the most difficult material presented in the readings of this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_efficacy3"].error_messages = {
            "required": u"Please answer the question: I'm confident I can understand the basic concepts taught in this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_efficacy4"].error_messages = {
            "required": u"Please answer the question: I'm confident I can understand the most complex material presented by the instructor in this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_efficacy5"].error_messages = {
            "required": u"Please answer the question: I'm confident I can do an excellent job on the assignments and tests in this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_efficacy6"].error_messages = {
            "required": u"Please answer the question: I expect to do well in this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_efficacy7"].error_messages = {
            "required": u"Please answer the question: I'm certain I can master the skills being taught in this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_efficacy8"].error_messages = {
            "required": u"Please answer the question: Considering the difficulty of this course, the teacher, and my skills, I think I will do well in this course.",
            "invalid": u"Likert answer is not valid.",
        }

        self.fields["scale_mnmgt_int1"].required = True
        self.fields["scale_mnmgt_int2"].required = True
        self.fields["scale_mnmgt_int3"].required = True
        self.fields["scale_mnmgt_int4"].required = True
        self.fields["scale_mnmgt_int5"].required = True
        self.fields["scale_mnmgt_int6"].required = True
        self.fields["scale_mnmgt_int7"].required = True
        self.fields["scale_mnmgt_int8"].required = True
        self.fields["scale_mnmgt_int9"].required = True
        self.fields["scale_mnmgt_int10"].required = True
        self.fields["scale_mnmgt_int11"].required = True
        self.fields["scale_mnmgt_int12"].required = True

        self.fields["scale_mnmgt_int1"].error_messages = {
            "required": u"Please answer the question: I usually study in a place where I can concentrate on my course work.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int2"].error_messages = {
            "required": u"Please answer the question: I make good use of my study time for this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int3"].error_messages = {
            "required": u"Please answer the question: I find it hard to stick to a study schedule.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int4"].error_messages = {
            "required": u"Please answer the question: I have a regular place set aside for studying.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int5"].error_messages = {
            "required": u"Please answer the question: I make sure I keep up with the weekly readings and assignments for this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int6"].error_messages = {
            "required": u"Please answer the question: I attend this course regularly.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int7"].error_messages = {
            "required": u"Please answer the question: I often find that I don't spend very much time on this course because of other activities.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int8"].error_messages = {
            "required": u"Please answer the question: I rarely find time to review my notes or readings before an exam.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int9"].error_messages = {
            "required": u"Please answer the question: I often feel so lazy or bored when I study for this course that I quit before I finish what I planned to do.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int10"].error_messages = {
            "required": u"Please answer the question: I work hard to do well in this course even if I don't like what we are doing.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int11"].error_messages = {
            "required": u"Please answer the question: I often feel so lazy or bored when I study for this course that I quit before I finish what I planned to do.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_mnmgt_int12"].error_messages = {
            "required": u"Please answer the question: Even when course materials are dull and uninteresting, I manage to keep working until I finish.",
            "invalid": u"Likert answer is not valid.",
        }

        self.fields["scale_cog1"].required = True
        self.fields["scale_cog2"].required = True
        self.fields["scale_cog3"].required = True
        self.fields["scale_cog4"].required = True
        self.fields["scale_cog5"].required = True
        self.fields["scale_cog6"].required = True
        self.fields["scale_cog7"].required = True
        self.fields["scale_cog8"].required = True

        self.fields["scale_cog1"].error_messages = {
            "required": u"Please answer the question: When I study the readings for this course, I outline the material to help me organize my thoughts.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_cog2"].error_messages = {
            "required": u"Please answer the question: When I study for this course, I go through the readings and my course notes and try to find the most important ideas.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_cog3"].error_messages = {
            "required": u"Please answer the question: I make simple charts, diagrams, or tables to help me organize course material.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_cog4"].error_messages = {
            "required": u"Please answer the question: When I study for this course, I go over my course notes and make an outline of important concepts.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_cog5"].error_messages = {
            "required": u"Please answer the question: When I study for this course, I practice saying the material to myself over and over.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_cog6"].error_messages = {
            "required": u"Please answer the question: When studying for this course, I read my course notes and the course readings over and over again.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_cog7"].error_messages = {
            "required": u"Please answer the question: I memorize key words to remind me of important concepts in this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_cog8"].error_messages = {
            "required": u"Please answer the question: I make lists of important terms for this course and memorize the lists.",
            "invalid": u"Likert answer is not valid.",
        }

        self.fields["scale_proc1"].required = True
        self.fields["scale_proc2"].required = True
        self.fields["scale_proc3"].required = True
        self.fields["scale_proc4"].required = True
        self.fields["scale_proc5"].required = True

        self.fields["scale_proc1"].error_messages = {
            "required": u"Please answer the question: I put off projects until the last minute.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_proc2"].error_messages = {
            "required": u"Please answer the question: I know I should work on course work, but I just don't do it.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_proc3"].error_messages = {
            "required": u"Please answer the question: I get distracted by other, more fun, things when I am supposed to work on course work.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_proc4"].error_messages = {
            "required": u"Please answer the question: When given an assignment, I usually put it away and forget about it until it is almost due.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_proc5"].error_messages = {
            "required": u"Please answer the question: I frequently find myself putting important deadlines off.",
            "invalid": u"Likert answer is not valid.",
        }

        self.fields["scale_big5_1"].required = True
        self.fields["scale_big5_2"].required = True

        self.fields["scale_big5_1"].error_messages = {
            "required": u"Please answer the question: I see myself as someone who tends to be lazy.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_big5_2"].error_messages = {
            "required": u"Please answer the question: I see myself as someone who does a thorough job.",
            "invalid": u"Likert answer is not valid.",
        }

        self.fields["scale_anxiety1"].required = True
        self.fields["scale_anxiety2"].required = True
        self.fields["scale_anxiety3"].required = True
        self.fields["scale_anxiety4"].required = True
        self.fields["scale_anxiety5"].required = True

        self.fields["scale_anxiety1"].error_messages = {
            "required": u"Please answer the question: When I take a test I think about how poorly I am doing compared with other students.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_anxiety2"].error_messages = {
            "required": u"Please answer the question: When I take a test I think about items on other parts of the test I can't answer.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_anxiety3"].error_messages = {
            "required": u"Please answer the question: When I take tests I think of the consequences of failing.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_anxiety4"].error_messages = {
            "required": u"Please answer the question: I have an uneasy, upset feeling when I take an exam.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_anxiety5"].error_messages = {
            "required": u"Please answer the question: I feel my heart beating fast when I take an exam.",
            "invalid": u"Likert answer is not valid.",
        }

        self.fields["scale_meta_cog1"].required = True
        self.fields["scale_meta_cog2"].required = True
        self.fields["scale_meta_cog3"].required = True
        self.fields["scale_meta_cog4"].required = True
        self.fields["scale_meta_cog5"].required = True
        self.fields["scale_meta_cog6"].required = True
        self.fields["scale_meta_cog7"].required = True
        self.fields["scale_meta_cog8"].required = True
        self.fields["scale_meta_cog8"].required = True
        self.fields["scale_meta_cog9"].required = True
        self.fields["scale_meta_cog10"].required = True
        self.fields["scale_meta_cog11"].required = True
        self.fields["scale_meta_cog12"].required = True

        self.fields["scale_meta_cog1"].error_messages = {
            "required": u"Please answer the question: During course time I often miss important points because I'm thinking of other things.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog2"].error_messages = {
            "required": u"Please answer the question: When reading for this course, I make up questions to help focus my reading.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog3"].error_messages = {
            "required": u"Please answer the question: When I become confused about something I'm reading for this course, I go back and try to figure it out.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog4"].error_messages = {
            "required": u"Please answer the question: If course material are difficult to understand, I change the way I read the material.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog5"].error_messages = {
            "required": u"Please answer the question: Before I study new course material thoroughly, I often skim it to see how it is organized.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog6"].error_messages = {
            "required": u"Please answer the question: I ask myself questions to make sure I understand the material I have been studying in this course.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog7"].error_messages = {
            "required": u"Please answer the question: I try to change the way I study in order to fit the course requirements and instructor's teaching style.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog8"].error_messages = {
            "required": u"Please answer the question: I often find that I have been reading for this course but don't know what it was all about.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog9"].error_messages = {
            "required": u"Please answer the question: I try to think through a topic and decide what I am supposed to learn from it rather than just reading it over when studying.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog10"].error_messages = {
            "required": u"Please answer the question: When studying for this course I try to determine which concepts I don't understand well.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog11"].error_messages = {
            "required": u"Please answer the question: When I study for this course, I set goals for myself in order to direct my activities in each study period.",
            "invalid": u"Likert answer is not valid.",
        }
        self.fields["scale_meta_cog12"].error_messages = {
            "required": u"Please answer the question: If I get confused taking notes in this course, I make sure I sort it out afterwards.",
            "invalid": u"Likert answer is not valid.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('enhanced_gender',
                  'study_programme',
                  'your_age',
                  'current_semester_of_study',
                  'part_time_student',
                  'bachelor_level_statistics',
                  'master_level_statistics',
                  'familiar_with_R',
                  'importance_DAEI',  # Likert
                  'motivation_DAEI',  # Likert
                  'measure_self_set_goals',  # Likert
                  'measure_around_you',  # Likert  #'course_how_many_students_studying', #'more_time_on_course',
                  'procrastinate',
                  'consent',
                  'list_zp1',
                  'list_zp2',
                  'list_zp3',
                  'list_kon1',
                  'list_kon2',
                  'list_kon3',
                  'list_reg1',
                  'list_reg2',
                  'list_reg3',
                  'scale_gradegoal1',
                  'scale_gradegoal2',
                  'scale_efficacy1',
                  'scale_efficacy2',
                  'scale_efficacy3',
                  'scale_efficacy4',
                  'scale_efficacy5',
                  'scale_efficacy6',
                  'scale_efficacy7',
                  'scale_efficacy8',
                  'scale_meta_cog1',
                  'scale_meta_cog2',
                  'scale_meta_cog3',
                  'scale_meta_cog4',
                  'scale_meta_cog5',
                  'scale_meta_cog6',
                  'scale_meta_cog7',
                  'scale_meta_cog8',
                  'scale_meta_cog9',
                  'scale_meta_cog10',
                  'scale_meta_cog11',
                  'scale_meta_cog12',
                  'scale_mnmgt_int1',
                  'scale_mnmgt_int2',
                  'scale_mnmgt_int3',
                  'scale_mnmgt_int4',
                  'scale_mnmgt_int5',
                  'scale_mnmgt_int6',
                  'scale_mnmgt_int7',
                  'scale_mnmgt_int8',
                  'scale_mnmgt_int9',
                  'scale_mnmgt_int10',
                  'scale_mnmgt_int11',
                  'scale_mnmgt_int12',
                  'scale_cog1',
                  'scale_cog2',
                  'scale_cog3',
                  'scale_cog4',
                  'scale_cog5',
                  'scale_cog6',
                  'scale_cog7',
                  'scale_cog8',
                  'scale_proc1',
                  'scale_proc2',
                  'scale_proc3',
                  'scale_proc4',
                  'scale_proc5',
                  'scale_big5_1',
                  'scale_big5_2',
                  'scale_anxiety1',
                  'scale_anxiety2',
                  'scale_anxiety3',
                  'scale_anxiety4',
                  'scale_anxiety5',
                  'list_lang',
                  )
        widgets = {
            'more_time_on_course': forms.TextInput(attrs={'size': 10}),
            'course_how_many_students_studying': forms.TextInput(attrs={'size': 10}),
        }
