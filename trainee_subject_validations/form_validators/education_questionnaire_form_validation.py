from edc_constants.constants import NO, YES
from edc_form_validators import FormValidator


class EducationQuestionnaireFormValidation(FormValidator):

    def clean(self):
        self.required_if(
            YES,
            field='currently_working',
            field_required='what_type_of_work',
        )
