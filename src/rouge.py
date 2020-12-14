from rouge import FilesRouge
import os
import os.path


hyp_path = "C:\\Users\\Admin\\Desktop\\virtual\\predicted_post.txt" 
ref_path = "C:\\Users\\Admin\\Desktop\\virtual\\answer_true_post.txt"



files_rouge = FilesRouge()
scores = files_rouge.get_scores(hyp_path, ref_path, avg=True)
print(scores) 