import sys
import os

class RecruitmentAgencyUtils():
	
	def get_pdf_files(self, folder_path:str) -> list[str]:
		pdf_files = []
		for file in os.listdir(folder_path):
			if file.lower().endswith('.pdf'):
				# token 'PDF_filename' used in tasks.yaml
				pdf_files.append(
					{
					"PDF_filename": os.path.join(folder_path, file)
					}
				)
		#print(pdf_files)
		return pdf_files
