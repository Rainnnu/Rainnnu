import pstats
import sys
import cProfile
import plagiarism_checker

def main (orig_path,plag_path,output_path):
    try :
        # 读取文件
        with open(orig_path,'r',encoding='utf-8') as f:
            orig_text = f.read()
        with open(plag_path,'r',encoding='utf-8') as f:
            plag_text = f.read()

        orig_words= plagiarism_checker.before_calculate(orig_text)
        plag_words= plagiarism_checker.before_calculate(plag_text)

        similarity = plagiarism_checker.similarity_calculate(orig_words, plag_words)

        # 输出结果到文件
        with open(output_path, 'a',encoding='utf-8') as f:
            f.write(f"文件{orig_path}与文件{plag_path}的相似度为{similarity:.2f}\n")
        # 输出结果到控制台
        print(f"相似度为{similarity:.2f}，结果已保存到 {output_path}")

    except Exception as e:
        print(f"发生错误：{e}")


if __name__=="__main__":
    if len(sys.argv)!=4:
        print("用法：python main.py <源文件路径> <抄袭文件路径> <分析结果路径>")
        sys.exit(1)

    # 从命令行获取参数
    orig_path = sys.argv[1]  # 原文文件路径
    plag_path = sys.argv[2]  # 抄袭版文件路径
    output_path = sys.argv[3]  # 输出文件路径

    main(orig_path,plag_path,output_path)