from edc_constants.constants import NO, YES
from edc_form_validators import FormValidator


class SubjectScreeningFormValidation(FormValidator):

    def clean(self):
        self.required_if(
            NO,
            field='citizen_or_not',
            field_required='married_to_motswana',
        )

        self.required_if(
            YES,
            field='married_to_motswana',
            field_required='marriage_certificate_proof',
        )

        self.required_if(
            NO,
            field='literate_or_illiterate',
            field_required='literate_witness',
        )


