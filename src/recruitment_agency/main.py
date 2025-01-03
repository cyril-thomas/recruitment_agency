#!/usr/bin/env python
import sys
import warnings

from recruitment_agency.crew import RecruitmentAgency
from recruitment_agency.utils import RecruitmentAgencyUtils

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = RecruitmentAgencyUtils().get_pdf_files("src/recruitment_agency/files")

    RecruitmentAgency().crew().kickoff_for_each(inputs=inputs)
