import sys
import os
from pydantic import BaseModel


class RecruitmentAgencyUtils:

    def get_pdf_files(self, folder_path: str) -> list[str]:
        pdf_files = []
        for file in os.listdir(folder_path):
            if file.lower().endswith(".pdf"):
                # token 'PDF_filename' used in tasks.yaml
                pdf_files.append({"PDF_filename": os.path.join(folder_path, file)})
        # print(pdf_files)
        return pdf_files


class Education(BaseModel):
    degree_certification_name: str
    type: str
    institution_name: str
    year_of_completion: str
    field_of_study_major: str
    address: str
    alternate_names: str


class Candidate(BaseModel):
    full_name: str
    education: list[Education]
