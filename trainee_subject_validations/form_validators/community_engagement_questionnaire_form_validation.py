from edc_constants.constants import NO, YES, OTHER
from edc_form_validators import FormValidator


class CommunityEngagementQuestionnaireFormValidation(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='major_problems',
            field_required='major_problems_other',
        )



