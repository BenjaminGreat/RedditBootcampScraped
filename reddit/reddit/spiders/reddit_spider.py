
from scrapy import Spider
from reddit.items import RedditItem


class RedditSpider(Spider):
	name = "reddit"
	allowed_urls = ['https://www.reddit.com']
	start_urls = ['https://www.reddit.com/r/datascience/comments/761xwo/are_data_science_bootcamps_worth_the_money/','https://www.reddit.com/r/datascience/comments/53desn/share_your_thoughts_about_the_explosion_of_data/','https://www.reddit.com/r/datascience/comments/67bb70/what_is_the_best_data_science_bootcamp/','https://www.reddit.com/r/cscareerquestions/comments/6arqif/thoughts_on_data_science_bootcamp/','https://www.reddit.com/r/datascience/comments/6e31pw/review_of_the_data_incubator_data_science_bootcamp/','https://www.reddit.com/r/UCI/comments/758o0o/uci_data_sciencebootcamp_or_bs/','https://www.reddit.com/r/rutgers/comments/64qtf2/data_science_bootcampcertificate/','https://www.reddit.com/r/datascience/comments/5m25tj/metis_vs_general_assembly_for_data_science/','https://www.reddit.com/r/MachineLearning/comments/3inq3c/should_i_pay_16k_for_a_data_science_bootcamp/','https://www.reddit.com/r/data/comments/3ovc54/metis_data_science_bootcamp_worth_14k/','https://www.reddit.com/r/datascience/comments/6uii3w/data_science_bootcamp_choice_galvanize_vs_general/','https://www.reddit.com/r/datascience/comments/3ex8kr/im_in_a_data_science_bootcamp_got_questions/','https://www.reddit.com/r/MachineLearning/comments/49lhf8/should_i_do_a_data_science_bootcamp/','https://www.reddit.com/r/datascience/comments/49ju3p/data_science_bootcamp_worth_going_into_debt_for/','https://www.reddit.com/r/datascience/comments/513k7b/prerequisites_for_data_science_bootcamps/','https://www.reddit.com/r/datascience/comments/4l3163/why_are_so_many_data_science_bootcamps_only_open/','https://www.reddit.com/r/datascience/comments/4rt8hy/just_graduated_from_metis_a_data_science_bootcamp/','https://www.reddit.com/r/korea/comments/4qnqm3/any_data_science_bootcamps_in_korea/','https://www.reddit.com/r/datascience/comments/5yl482/best_data_science_bootcamps_around_the_globe/','https://www.reddit.com/r/MLjobs/comments/6zpyi5/for_hire_data_science_bootcamp_graduate_in/','https://www.reddit.com/r/datascience/comments/49mpqv/what_are_your_thoughts_on_the_galvanize_data/','https://www.reddit.com/r/datascience/comments/5xpucn/data_science_bootcamp_review/','https://www.reddit.com/r/datascience/comments/4xhjlo/is_austin_galvanize_data_science_bootcamp_worth_it/','https://www.reddit.com/r/DataScienceJobs/comments/6ojas0/hiring_data_science_bootcamp_mentor_remote_paid/','https://www.reddit.com/r/cscareerquestions/comments/3ld88z/thinking_of_quitting_my_job_as_a_dev_at_a_big_4/','https://www.reddit.com/r/datascience/comments/3qhfxe/data_science_bootcamps_which_one_would_you/','https://www.reddit.com/r/gis/comments/5ajdex/geospatial_data_science_bootcamp/','https://www.reddit.com/r/BigDataJobs/comments/4gej1c/data_science_bootcamps/','https://www.reddit.com/r/datascience/comments/4kwhkd/is_a_masters_in_one_field_combined_with_a_data/','https://www.reddit.com/r/datascience/comments/43g1rq/opinions_on_data_science_bootcamp_bundle_from/','https://www.reddit.com/r/MachineLearning/comments/2apjhl/metis_data_science_bootcamp_accepting/','https://www.reddit.com/r/datascience/comments/47alfd/can_associates_degree_in_mathematics_data_science/','https://www.reddit.com/r/MachineLearning/comments/2rshn1/12week_data_science_bootcamp/','https://www.reddit.com/r/datascience/comments/2xcpen/from_academia_to_metis_data_science_bootcamp_andy/','https://www.reddit.com/r/datascience/comments/2rrzq1/12week_data_science_bootcamp_invitation/','https://www.reddit.com/r/findareddit/comments/3f1bfx/a_subreddit_to_ask_about_data_science_bootcamps/','https://www.reddit.com/r/codingbootcamp/comments/5mweb9/level_of_experience_for_data_science_bootcamp/','https://www.reddit.com/r/bigdata/comments/4q8juo/whats_hot_this_summer_data_science_bootcamps/','https://www.reddit.com/r/datascience/comments/4dt7la/galvanize_data_science_bootcamp_scholarships/','https://www.reddit.com/r/cscareerquestions/comments/49lnaj/given_my_background_should_i_do_a_data_science/','https://www.reddit.com/r/cscareerquestions/comments/2b8zq5/data_science_bootcamp_would_i_be_able_to_get_a/','https://www.reddit.com/r/datascience/comments/3f6pab/thoughts_on_data_science_programs_or_bootcamps_vs/','https://www.reddit.com/r/DataScientist/comments/68rvm6/which_data_scientist_bootcamp_should_i_take/','https://www.reddit.com/r/learnprogramming/comments/5hzjcb/im_a_data_scientist_who_transitioned_to_the_field/','https://www.reddit.com/r/datascience/comments/5jbo9u/data_science_career_questions_thread_dec_2016/','https://www.reddit.com/r/datascience/comments/4mxdsi/data_science_career_questions_thread_20160607/','https://www.reddit.com/r/datascience/comments/67anrc/request_feedback_on_my_resume_for_data_science/','https://www.reddit.com/r/datascience/comments/4dw47r/data_science_career_questions_thread_20160408/','https://www.reddit.com/r/datascience/comments/4gz3mc/data_science_career_questions_thread_20160429/','https://www.reddit.com/r/datascience/comments/6zu2df/seeking_some_other_opinions_on_pursuing_data/','https://www.reddit.com/r/datascience/comments/4ewfhh/data_science_career_questions_thread_20160415/','https://www.reddit.com/r/datascience/comments/4jp4o1/data_science_career_questions_thread_20160516/','https://www.reddit.com/r/personalfinance/comments/6px9n6/25m_debating_on_taking_loan_for_university_data/','https://www.reddit.com/r/datascience/comments/4fykh9/data_science_career_questions_thread_20160422/','https://www.reddit.com/r/datascience/comments/72namy/thinkful_data_science/','https://www.reddit.com/r/datascience/comments/54mtmp/msc_complex_systems_modelling_or_msc_data_science/','https://www.reddit.com/r/datascience/comments/5p7r5z/hoping_to_get_some_advice_on_the_value_of_getting/','https://www.reddit.com/r/datascience/comments/3eqf7t/important_career_change_decision_into_data_science/','https://www.reddit.com/r/datascience/comments/3ubn4g/data_science_dojo_worthwhile_advice_for_a_new_phd/','https://www.reddit.com/r/cscareerquestions/comments/43pg8w/can_someone_hack_their_way_into_data_science/','https://www.reddit.com/r/datascience/comments/75i7zo/ballpark_placement_rate_coming_out_of_ds_bootcamps/','https://www.reddit.com/r/bioinformatics/comments/5upf2a/coding_bootcamp_for_bioinformatics/','https://www.reddit.com/r/datascience/comments/786y9g/us_bootcamps_that_require_authorization_to_work/','https://www.reddit.com/r/datascience/comments/5wsvb4/advice_needed_bootcamp_in_addition_to_masters/','https://www.reddit.com/r/learnprogramming/comments/6anjpa/what_are_your_thoughts_on_a_cs_degree_online_from/','https://www.reddit.com/r/cscareerquestions/comments/3s86sw/how_would_experience_teaching_at_a_bootcamp_be/','https://www.reddit.com/r/datascience/comments/6g4usu/how_many_companies_actually_have_big_data/','https://www.reddit.com/r/cscareerquestions/comments/6jvjr3/which_track_to_pursue_data_scientist_having/','https://www.reddit.com/r/datascience/comments/60ztri/data_scientists_in_the_bay_area_id_love_to_learn/','https://www.reddit.com/r/datascience/comments/5omy8s/suggestions_on_courses_to_become_a_data_scientist/','https://www.reddit.com/r/SeaJobs/comments/64mno5/for_hire_junior_data_analystscientist_in_seattle/','https://www.reddit.com/r/cscareerquestions/comments/5on8s4/suggestions_on_courses_to_become_a_data_scientist/','https://www.reddit.com/r/BigDataJobs/comments/4fmc4b/four_routes_to_becoming_a_data_scientist_big_cloud/','https://www.reddit.com/r/datascience/comments/339ppi/in_the_last_year_ive_finished_three_datascience/','https://www.reddit.com/r/selfimprovement/comments/72e9v7/need_help_on_improving_myself_with_learning/','https://www.reddit.com/r/cscareerquestions/comments/6y6gsx/analyst_dev_eng_what_am_i/','https://www.reddit.com/r/ENFP/comments/66j91z/enfps_being_impatient/','https://www.reddit.com/r/Udacity/comments/726iis/deciding_between_udacity_nanodegree_or_georgia/','https://www.reddit.com/r/bioinformatics/comments/5oksws/transitioning_from_biology_to_more_computational/','https://www.reddit.com/r/datascience/comments/6fxc3n/advice_for_a_web_analytics_guru_aspiring_to/','https://www.reddit.com/r/datascience/comments/64kr6g/i_have_a_capstone_project_that_im_going_to_be/','https://www.reddit.com/r/ITCareerQuestions/comments/6y6k35/analyst_dev_eng_what_am_i/','https://www.reddit.com/r/datascience/comments/6ufyku/any_new_tdi_fellows/','https://www.reddit.com/r/datascience/comments/35v1av/beeing_recognised_based_on_online_courses_and/','https://www.reddit.com/r/datascience/comments/3tnw6j/laptops/','https://www.reddit.com/r/datascience/comments/3rtf3z/experience_with_startupml/','https://www.reddit.com/r/datascience/comments/2y6yp2/careers_in_digital_advertising/','https://www.reddit.com/r/webdev/comments/4hzkp0/new_data_from_stack_overflow_shows_bootcamp_grads/','https://www.reddit.com/r/datascience/comments/5z14yo/nyc_data_science_academy_bootcamp_did_any_of_you/','https://www.reddit.com/r/datascience/comments/727b93/need_help_choosing_between_ms_in_data_science_and/','https://www.reddit.com/r/torrentrequests/comments/6lzl0q/python_data_science_and_machine_learning_bootcamp/','https://www.reddit.com/r/datascience/comments/3y4v10/which_is_better_data_science_masters_program_eg/','https://www.reddit.com/r/datascience/comments/6wsztl/advice_choosing_between_data_analytics_bootcamp/','https://www.reddit.com/r/datascience/comments/3yb0w9/which_data_science_masters_to_apply_for_with_my/','https://www.reddit.com/r/learnprogramming/comments/6nbkf0/employer_has_training_budget_that_resets_every/','https://www.reddit.com/r/datascience/comments/60mg75/first_data_science_job_as_a_bootcamp_instructor_a/','https://www.reddit.com/r/Python/comments/6djei6/python_for_data_science_and_machine_learning/','https://www.reddit.com/r/learndatascience/comments/4n6r9z/a_guide_to_24_major_coding_bootcamps_that_cuts/','https://www.reddit.com/r/learnprogramming/comments/4k8pha/interested_in_taking_a_pricey_bootcamp_course_for/','https://www.reddit.com/r/Serendipity/comments/3y97ey/which_is_better_data_science_masters_program_eg/','https://www.reddit.com/r/datasciencenews/comments/4bq66o/get_paid_to_be_a_data_science_mentor_for_an_mit/','https://www.reddit.com/r/datascience/comments/2w43s6/nyc_data_science_academy_12week_bootcamp_june_1/','https://www.reddit.com/r/datascience/comments/4az8ha/what_data_sciece_bootcamp_do_you_recommend/','https://www.reddit.com/r/datascience/comments/6i2rw0/any_newbies_have_questions_about_getting_into/','https://www.reddit.com/r/datascience/comments/664uxn/my_curriculumschedule_to_get_from_zero_to_data/','https://www.reddit.com/r/cscareerquestions/comments/34824q/physicscomputational_science_grad_school_or/','https://www.reddit.com/r/autotldr/comments/3s3ep8/coding_bootcamps_are_diminishing_traditional/']

	def parse(self, response):
		#comment = response.xpath("//div[@class='usertext-body may-blank-within md-container']/div/text()").extract()
		#comment = response.xpath("//*[@id='form-t1_d7sgs6ywxr']/div/div/text()").extract()
		


		#rows = response.xpath('//div[@class="md"]/p').extract()
		#for row in rows[5:11]: 
		comments =  response.xpath('//div[@class="md"]/p/text()')[5:400].extract()
			#comment2 =  response.xpath('//div[@class="md"]/p')[6].extract()
			#comment3 =  response.xpath('//div[@class="md"]/p')[7].extract()
		
		item =RedditItem()
		item['comments'] = comments
		#item['comment2'] = comment2
		#item['comment3'] = comment3
		yield item 

      