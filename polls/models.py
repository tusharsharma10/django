# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class Companies(models.Model):
#     companyid = models.AutoField(db_column='CompanyId', primary_key=True)  # Field name made lowercase.
#     name = models.CharField(db_column='Name', max_length=191, blank=True, null=True)  # Field name made lowercase.
#     industryid = models.IntegerField(db_column='IndustryId')  # Field name made lowercase.
#     urlname = models.CharField(db_column='UrlName', max_length=160, blank=True, null=True)  # Field name made lowercase.
#     views = models.IntegerField(db_column='Views')  # Field name made lowercase.
#     shortname = models.CharField(db_column='ShortName', max_length=191, blank=True, null=True)  # Field name made lowercase.
#     logo = models.CharField(db_column='Logo', max_length=500, blank=True, null=True)  # Field name made lowercase.
#     modified = models.DateTimeField(db_column='Modified')  # Field name made lowercase.
#     created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
#     locked = models.IntegerField(db_column='Locked')  # Field name made lowercase.
#     sectorid = models.IntegerField(db_column='SectorId')  # Field name made lowercase.
#     glassdoorid = models.IntegerField(db_column='GlassdoorId', blank=True, null=True)  # Field name made lowercase.
#     rating = models.FloatField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
#     processedcompname = models.CharField(db_column='ProcessedCompName', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     prcessedshortname = models.CharField(db_column='PrcessedShortName', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     followerscount = models.IntegerField(db_column='followersCount', blank=True, null=True)  # Field name made lowercase.
#     verified = models.IntegerField(db_column='Verified', blank=True, null=True)  # Field name made lowercase.
#     naukriid = models.IntegerField(db_column='NaukriId', blank=True, null=True)  # Field name made lowercase.
#     closed = models.IntegerField(db_column='Closed', blank=True, null=True)  # Field name made lowercase.
#     shit = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'companies'
#
#
# class Ds2(models.Model):
#     id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'ds2'
#
#
# class Ds3(models.Model):
#     id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'ds3'
#
#
# class Ds5(models.Model):
#     id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'ds5'
#
#
# class Ds6(models.Model):
#     id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'ds6'
#
#
# class Ds7(models.Model):
#     id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'ds7'
#
#
# class DumpShit(models.Model):
#
#     class Meta:
#         managed = False
#         db_table = 'dump_shit'
#
#
# class ReviewSummariesChatgpt(models.Model):
#     startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
#     enddate = models.DateField(db_column='endDate')  # Field name made lowercase.
#     sentiment = models.IntegerField(db_column='Sentiment')  # Field name made lowercase.
#     reviewids = models.JSONField(db_column='reviewIds', blank=True, null=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='companyId')  # Field name made lowercase.
#     chatgptresponse5lines = models.JSONField(db_column='chatgptresponse5Lines', blank=True, null=True)  # Field name made lowercase.
#     chatgpttags = models.JSONField(db_column='chatgptTags', blank=True, null=True)  # Field name made lowercase.
#     chatgpttagindexesinreviews = models.JSONField(db_column='chatgptTagIndexesInReviews', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'review_summaries_chatgpt'
#
#
# class TestShit(models.Model):
#     id = models.IntegerField(blank=True, null=True)
#     shitfloat = models.FloatField(db_column='shitFloat', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'test_shit'


class Transactions(models.Model):
    txnid = models.IntegerField(db_column='txnId', primary_key=True)  # Field name made lowercase.
    code = models.CharField(max_length=20, blank=True, null=True)
    companyid = models.IntegerField(db_column='companyId', blank=True, null=True)  # Field name made lowercase.
    jobprofileid = models.IntegerField(db_column='jobProfileId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transactions'


# class UserBenefitsContributions(models.Model):
#     userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
#     clientid = models.CharField(db_column='clientId', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     companyname = models.CharField(db_column='companyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     companyid = models.IntegerField(db_column='companyId', blank=True, null=True)  # Field name made lowercase.
#     jobprofilename = models.CharField(db_column='jobProfileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     jobprofileid = models.IntegerField(db_column='jobProfileId', blank=True, null=True)  # Field name made lowercase.
#     overallrating = models.IntegerField(db_column='overallRating', blank=True, null=True)  # Field name made lowercase.
#     workpolicy = models.CharField(db_column='workPolicy', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fb_performancebonusoffered = models.IntegerField(db_column='fb_performanceBonusOffered', blank=True, null=True)  # Field name made lowercase.
#     fb_performancebonusdata_payout = models.CharField(db_column='fb_performanceBonusData_payout', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     fb_performancebonusdata_amount = models.IntegerField(db_column='fb_performanceBonusData_amount', blank=True, null=True)  # Field name made lowercase.
#     fb_performancebonusdata_otherinfo = models.TextField(db_column='fb_performanceBonusData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     fb_joiningbonusoffered = models.IntegerField(db_column='fb_joiningBonusOffered', blank=True, null=True)  # Field name made lowercase.
#     fb_joiningbonusdata_amount = models.IntegerField(db_column='fb_joiningBonusData_amount', blank=True, null=True)  # Field name made lowercase.
#     fb_joiningbonusdata_otherinfo = models.TextField(db_column='fb_joiningBonusData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     fb_relocationbonusoffered = models.IntegerField(db_column='fb_relocationBonusOffered', blank=True, null=True)  # Field name made lowercase.
#     fb_relocationbonusdata_amount = models.IntegerField(db_column='fb_relocationBonusData_amount', blank=True, null=True)  # Field name made lowercase.
#     fb_relocationbonusdata_otherinfo = models.TextField(db_column='fb_relocationBonusData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     fb_stocksoffered = models.IntegerField(db_column='fb_stocksOffered', blank=True, null=True)  # Field name made lowercase.
#     fb_stocksdata_stocktype = models.CharField(db_column='fb_stocksData_stockType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fb_stocksdata_amount = models.IntegerField(db_column='fb_stocksData_amount', blank=True, null=True)  # Field name made lowercase.
#     fb_stocksdata_vestingperiod = models.CharField(db_column='fb_stocksData_vestingPeriod', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fb_stocksdata_vestingpercentage = models.CharField(db_column='fb_stocksData_vestingPercentage', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fb_stocksdata_otherinfo = models.TextField(db_column='fb_stocksData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     fb_mobilebillreimbursementoffered = models.IntegerField(db_column='fb_mobileBillReimbursementOffered', blank=True, null=True)  # Field name made lowercase.
#     fb_retirementbenefitsoffered = models.IntegerField(db_column='fb_retirementBenefitsOffered', blank=True, null=True)  # Field name made lowercase.
#     fb_retirementbenefitsdata_type = models.CharField(db_column='fb_retirementBenefitsData_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fb_retirementbenefitsdata_otherinfo = models.TextField(db_column='fb_retirementBenefitsData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     fb_carleaseoffered = models.IntegerField(db_column='fb_carLeaseOffered', blank=True, null=True)  # Field name made lowercase.
#     fb_otherfinancialbenefits = models.TextField(db_column='fb_otherFinancialBenefits', blank=True, null=True)  # Field name made lowercase.
#     hib_healthinsuranceoffered = models.IntegerField(db_column='hib_healthInsuranceOffered', blank=True, null=True)  # Field name made lowercase.
#     hib_healthinsurancedata_amount = models.IntegerField(db_column='hib_healthInsuranceData_amount', blank=True, null=True)  # Field name made lowercase.
#     hib_healthinsurancedata_noofdependents = models.IntegerField(db_column='hib_healthInsuranceData_noOfDependents', blank=True, null=True)  # Field name made lowercase.
#     hib_healthinsurancedata_parentsincluded = models.IntegerField(db_column='hib_healthInsuranceData_parentsIncluded', blank=True, null=True)  # Field name made lowercase.
#     hib_healthinsurancedata_otherinfo = models.TextField(db_column='hib_healthInsuranceData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     hib_lifeinsuranceoffered = models.IntegerField(db_column='hib_lifeInsuranceOffered', blank=True, null=True)  # Field name made lowercase.
#     hib_lifeinsurancedata_amount = models.IntegerField(db_column='hib_lifeInsuranceData_amount', blank=True, null=True)  # Field name made lowercase.
#     hib_lifeinsurancedata_otherinfo = models.TextField(db_column='hib_lifeInsuranceData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     hib_annualheathcheckupoffered = models.IntegerField(db_column='hib_annualHeathCheckupOffered', blank=True, null=True)  # Field name made lowercase.
#     hib_mentalheathwellbeingoffered = models.IntegerField(db_column='hib_mentalheathWellbeingOffered', blank=True, null=True)  # Field name made lowercase.
#     hib_mentalheathwellbeingdata_counsellingtype = models.CharField(db_column='hib_mentalheathWellbeingData_counsellingType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hib_mentalheathwellbeingdata_otherinfo = models.TextField(db_column='hib_mentalheathWellbeingData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     hib_gymmembershipoffered = models.IntegerField(db_column='hib_gymMembershipOffered', blank=True, null=True)  # Field name made lowercase.
#     hib_otherhealthinsurancebenefits = models.CharField(db_column='hib_otherHealthInsuranceBenefits', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     opb_officeconveyanceoffered = models.IntegerField(db_column='opb_officeConveyanceOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_officeconveyancedata_offeringtype = models.CharField(db_column='opb_officeConveyanceData_offeringType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     opb_officeconveyancedata_otherinfo = models.TextField(db_column='opb_officeConveyanceData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     opb_childcareoffered = models.IntegerField(db_column='opb_childCareOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_cafeteriaoffered = models.IntegerField(db_column='opb_cafeteriaOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_freemealoffered = models.IntegerField(db_column='opb_freeMealOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_freemealdata_freemealtype = models.CharField(db_column='opb_freeMealData_freeMealType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     opb_freemealdata_subsidisedmealoffered = models.IntegerField(db_column='opb_freeMealData_subsidisedMealOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_freemealdata_otherinfo = models.TextField(db_column='opb_freeMealData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     opb_recreationalactivitiesoffered = models.IntegerField(db_column='opb_recreationalActivitiesOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_recreationalactivitiesdata_activitytype = models.CharField(db_column='opb_recreationalActivitiesData_activityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     opb_recreationalactivitiesdata_otherinfo = models.TextField(db_column='opb_recreationalActivitiesData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     opb_joininggoodiesoffered = models.IntegerField(db_column='opb_joiningGoodiesOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_festivalgiftsoffered = models.IntegerField(db_column='opb_festivalGiftsOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_officegymoffered = models.IntegerField(db_column='opb_officeGymOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_wfhsetupoffered = models.IntegerField(db_column='opb_wfhSetupOffered', blank=True, null=True)  # Field name made lowercase.
#     opb_wfhsetupdata_otherinfo = models.TextField(db_column='opb_wfhSetupData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     opb_otherofficeperksbenefits = models.CharField(db_column='opb_otherOfficePerksBenefits', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tob_annualleavesoffered = models.IntegerField(db_column='tob_annualLeavesOffered', blank=True, null=True)  # Field name made lowercase.
#     tob_annualleavesdata_noofleaves = models.CharField(db_column='tob_annualLeavesData_noOfLeaves', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tob_annualleavesdata_unlimitedleavesoffered = models.IntegerField(db_column='tob_annualLeavesData_unlimitedLeavesOffered', blank=True, null=True)  # Field name made lowercase.
#     tob_annualleavesdata_otherinfo = models.TextField(db_column='tob_annualLeavesData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     tob_maternityleavesoffered = models.IntegerField(db_column='tob_maternityLeavesOffered', blank=True, null=True)  # Field name made lowercase.
#     tob_maternityleavesdata_timeperiod = models.CharField(db_column='tob_maternityLeavesData_timePeriod', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tob_maternityleavesdata_otherinfo = models.TextField(db_column='tob_maternityLeavesData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     tob_paternityleavesoffered = models.IntegerField(db_column='tob_paternityLeavesOffered', blank=True, null=True)  # Field name made lowercase.
#     tob_paternityleavesdata_timeperiod = models.CharField(db_column='tob_paternityLeavesData_timePeriod', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tob_paternityleavesdata_otherinfo = models.TextField(db_column='tob_paternityLeavesData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     tob_sabbaticaloffered = models.IntegerField(db_column='tob_sabbaticalOffered', blank=True, null=True)  # Field name made lowercase.
#     tob_sabbaticaldata_timeperiod = models.CharField(db_column='tob_sabbaticalData_timePeriod', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tob_sabbaticaldata_sabbaticaltype = models.CharField(db_column='tob_sabbaticalData_sabbaticalType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tob_sabbaticaldata_otherinfo = models.TextField(db_column='tob_sabbaticalData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     tob_othertimeoffbenefits = models.CharField(db_column='tob_otherTimeOffBenefits', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pslb_skilltrainingoffered = models.IntegerField(db_column='pslb_skillTrainingOffered', blank=True, null=True)  # Field name made lowercase.
#     pslb_offsiteexposureoffered = models.IntegerField(db_column='pslb_offsiteExposureOffered', blank=True, null=True)  # Field name made lowercase.
#     pslb_offsiteexposuredata_offsitetype = models.CharField(db_column='pslb_offsiteExposureData_offsiteType', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pslb_offsiteexposuredata_otherinfo = models.TextField(db_column='pslb_offsiteExposureData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     pslb_rewardsoffered = models.IntegerField(db_column='pslb_rewardsOffered', blank=True, null=True)  # Field name made lowercase.
#     pslb_rewardsdata_otherinfo = models.TextField(db_column='pslb_rewardsData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     pslb_coursereimbursementsoffered = models.IntegerField(db_column='pslb_courseReimbursementsOffered', blank=True, null=True)  # Field name made lowercase.
#     pslb_coursereimbursementsdata_otherinfo = models.TextField(db_column='pslb_courseReimbursementsData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     pslb_degreeassistanceoffered = models.IntegerField(db_column='pslb_degreeAssistanceOffered', blank=True, null=True)  # Field name made lowercase.
#     pslb_degreeassistancedata_otherinfo = models.TextField(db_column='pslb_degreeAssistanceData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     pslb_otherprofessionalsupportlearningbenefits = models.CharField(db_column='pslb_otherProfessionalSupportLearningBenefits', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bestbenefit = models.CharField(db_column='bestBenefit', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     worstbenefit = models.CharField(db_column='worstBenefit', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     totalworkex = models.IntegerField(db_column='totalWorkEx', blank=True, null=True)  # Field name made lowercase.
#     departmentname = models.CharField(db_column='departmentName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     departmentid = models.IntegerField(db_column='departmentId', blank=True, null=True)  # Field name made lowercase.
#     rolecategoryid = models.IntegerField(db_column='roleCategoryId', blank=True, null=True)  # Field name made lowercase.
#     rolecategoryname = models.CharField(db_column='roleCategoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     submit = models.IntegerField(blank=True, null=True)
#     utmcampaign = models.CharField(db_column='utmCampaign', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     utmmedium = models.CharField(db_column='utmMedium', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     utmsource = models.CharField(db_column='utmSource', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     created = models.DateTimeField(blank=True, null=True)
#     modified = models.DateTimeField(blank=True, null=True)
#     submittedon = models.DateTimeField(db_column='submittedOn', blank=True, null=True)  # Field name made lowercase.
#     secretkey = models.CharField(db_column='secretKey', max_length=55, blank=True, null=True)  # Field name made lowercase.
#     locationid = models.IntegerField(db_column='locationId', blank=True, null=True)  # Field name made lowercase.
#     locationname = models.CharField(db_column='locationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     fb_mobilebillreimbursementdata_otherinfo = models.TextField(db_column='fb_mobileBillReimbursementData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     fb_carleasedata_otherinfo = models.TextField(db_column='fb_carLeaseData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     hib_annualheathcheckupdata_otherinfo = models.TextField(db_column='hib_annualHeathCheckupData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     hib_gymmembershipdata_otherinfo = models.TextField(db_column='hib_gymMembershipData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     opb_childcaredata_otherinfo = models.TextField(db_column='opb_childCareData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     opb_cafeteriadata_otherinfo = models.TextField(db_column='opb_cafeteriaData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     opb_festivalgiftsdata_otherinfo = models.TextField(db_column='opb_festivalGiftsData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     opb_recreationalactivitiesdata_otheractivitytype = models.TextField(db_column='opb_recreationalActivitiesData_otherActivityType', blank=True, null=True)  # Field name made lowercase.
#     tob_maternityleavesdata_othertimeperiod = models.CharField(db_column='tob_maternityLeavesData_otherTimePeriod', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tob_paternityleavesdata_othertimeperiod = models.CharField(db_column='tob_paternityLeavesData_otherTimePeriod', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     pslb_skilltrainingdata_otherinfo = models.TextField(db_column='pslb_skillTrainingData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     pslb_offsiteexposuredata_otheroffsitetype = models.TextField(db_column='pslb_offsiteExposureData_otherOffSiteType', blank=True, null=True)  # Field name made lowercase.
#     opb_joininggoodiesdata_otherinfo = models.TextField(db_column='opb_joiningGoodiesData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     opb_officegymdata_otherinfo = models.TextField(db_column='opb_officeGymData_otherInfo', blank=True, null=True)  # Field name made lowercase.
#     status = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'user_benefits_contributions'
