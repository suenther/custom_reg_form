from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

from custom_reg_form.models import ExtraInfo


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consent', ExtraInfo.consent),
                ('study_programme', ExtraInfo.study_programme),
                ('enhanced_gender', ExtraInfo.enhanced_gender),
                ('current_semester_of_study', ExtraInfo.current_semester_of_study),
                ('part_time_student', ExtraInfo.part_time_student),
                ('bachelor_level_statistics', ExtraInfo.bachelor_level_statistics),
                ('master_level_statistics', ExtraInfo.master_level_statistics),
                ('familiar_with_R', ExtraInfo.familiar_with_R),
                ('importance_DAEI', ExtraInfo.importance_DAEI),
                ('motivation_DAEI', ExtraInfo.motivation_DAEI),
                ('procrastinate', ExtraInfo.procrastinate),
                ('measure_self_set_goals', ExtraInfo.measure_self_set_goals),
                ('measure_around_you', ExtraInfo.measure_around_you),
                ('more_time_on_course', ExtraInfo.more_time_on_course),
                ('course_how_many_students_studying', ExtraInfo.course_how_many_students_studying),
                ('list_zp1', ExtraInfo.list_zp1),
                ('list_zp2', ExtraInfo.list_zp2),
                ('list_zp3', ExtraInfo.list_zp3),
                ('list_kon1', ExtraInfo.list_kon1),
                ('list_kon2', ExtraInfo.list_kon2),
                ('list_kon3', ExtraInfo.list_kon3),
                ('list_reg1', ExtraInfo.list_reg1),
                ('list_reg2', ExtraInfo.list_reg2),
                ('list_reg3', ExtraInfo.list_reg3),
                ('list_lang', ExtraInfo.list_lang),
                ('scale_gradegoal1', ExtraInfo.scale_gradegoal1),
                ('scale_gradegoal2', ExtraInfo.scale_gradegoal2),
                ('your_age', ExtraInfo.your_age),

                ('scale_efficacy1', ExtraInfo.scale_efficacy1),
                ('scale_efficacy2', ExtraInfo.scale_efficacy2),
                ('scale_efficacy3', ExtraInfo.scale_efficacy3),
                ('scale_efficacy4', ExtraInfo.scale_efficacy4),
                ('scale_efficacy5', ExtraInfo.scale_efficacy5),
                ('scale_efficacy6', ExtraInfo.scale_efficacy6),
                ('scale_efficacy7', ExtraInfo.scale_efficacy7),
                ('scale_efficacy8', ExtraInfo.scale_efficacy8),

                ('scale_meta_cog1', ExtraInfo.scale_meta_cog1),
                ('scale_meta_cog2', ExtraInfo.scale_meta_cog2),
                ('scale_meta_cog3', ExtraInfo.scale_meta_cog3),
                ('scale_meta_cog4', ExtraInfo.scale_meta_cog4),
                ('scale_meta_cog5', ExtraInfo.scale_meta_cog5),
                ('scale_meta_cog6', ExtraInfo.scale_meta_cog6),
                ('scale_meta_cog7', ExtraInfo.scale_meta_cog7),
                ('scale_meta_cog8', ExtraInfo.scale_meta_cog8),
                ('scale_meta_cog9', ExtraInfo.scale_meta_cog9),
                ('scale_meta_cog10', ExtraInfo.scale_meta_cog10),
                ('scale_meta_cog11', ExtraInfo.scale_meta_cog11),
                ('scale_meta_cog12', ExtraInfo.scale_meta_cog12),

                ('scale_mnmgt_int1', ExtraInfo.scale_mnmgt_int1),
                ('scale_mnmgt_int2', ExtraInfo.scale_mnmgt_int2),
                ('scale_mnmgt_int3', ExtraInfo.scale_mnmgt_int3),
                ('scale_mnmgt_int4', ExtraInfo.scale_mnmgt_int4),
                ('scale_mnmgt_int5', ExtraInfo.scale_mnmgt_int5),
                ('scale_mnmgt_int6', ExtraInfo.scale_mnmgt_int6),
                ('scale_mnmgt_int7', ExtraInfo.scale_mnmgt_int7),
                ('scale_mnmgt_int8', ExtraInfo.scale_mnmgt_int8),
                ('scale_mnmgt_int9', ExtraInfo.scale_mnmgt_int9),
                ('scale_mnmgt_int10', ExtraInfo.scale_mnmgt_int10),
                ('scale_mnmgt_int11', ExtraInfo.scale_mnmgt_int11),
                ('scale_mnmgt_int12', ExtraInfo.scale_mnmgt_int12),

                ('scale_cog1', ExtraInfo.scale_cog1),
                ('scale_cog2', ExtraInfo.scale_cog2),
                ('scale_cog3', ExtraInfo.scale_cog3),
                ('scale_cog4', ExtraInfo.scale_cog4),
                ('scale_cog5', ExtraInfo.scale_cog5),
                ('scale_cog6', ExtraInfo.scale_cog6),
                ('scale_cog7', ExtraInfo.scale_cog7),
                ('scale_cog8', ExtraInfo.scale_cog8),

                ('scale_proc1', ExtraInfo.scale_proc1),
                ('scale_proc2', ExtraInfo.scale_proc2),
                ('scale_proc3', ExtraInfo.scale_proc3),
                ('scale_proc4', ExtraInfo.scale_proc4),
                ('scale_proc5', ExtraInfo.scale_proc5),

                ('scale_big5_1', ExtraInfo.scale_big5_1),
                ('scale_big5_2', ExtraInfo.scale_big5_2),

                ('scale_anxiety1', ExtraInfo.scale_anxiety1),
                ('scale_anxiety2', ExtraInfo.scale_anxiety2),
                ('scale_anxiety3', ExtraInfo.scale_anxiety3),
                ('scale_anxiety4', ExtraInfo.scale_anxiety4),
                ('scale_anxiety5', ExtraInfo.scale_anxiety5),

                ('user',
                 models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user+',
                                      to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
