import argparse
import pathlib


def get_args():
    parser = argparse.ArgumentParser(
        description="This is atcoder blog template")

    parser.add_argument('-d', '--directory', type=str,
                        help='This is episode directory.',
                        required=True)
    return parser.parse_args()


def list_to_text(input_list):
    with open("output_text.txt", 'w', encoding="utf-8") as f:
        for line in input_list:
            f.write("%s\n" % line)


def make_atcoder_url(episode_directory):
    result_list = []
    atcoder_root_url = "https://atcoder.jp/contests/" + episode_directory
    hatena_blog_embed = ":embed:cite"
    result_list.append("[" + atcoder_root_url + hatena_blog_embed+"]")

    p_pathlib = pathlib.Path(episode_directory)
    file_iter = p_pathlib.glob("**/*.py")
    file_list = []
    for file_name in file_iter:
        result_list.append("# [" + atcoder_root_url +
                           "/tasks/" + episode_directory +
                           "_" + file_name.stem + ":title]")
        file_list.append(str(file_name))

    return file_list, result_list


def main():
    args = get_args()
    print("Output the {} to output_text.txt".format(args.directory))

    file_iter, section_questions = make_atcoder_url(args.directory)
    file_list = list(file_iter)

    blog_sentence = []
    blog_sentence.append("## はじめに")
    blog_sentence.append("AtCoder Beginner Contest 000の振り返りをします。")

    # insert section
    for i, each_section in enumerate(section_questions):
        if i == 0:
            blog_sentence.append(each_section)
            blog_sentence.append("<!-- more -->")
            blog_sentence.append("[:contents]")
        else:
            blog_sentence.append(each_section)
            blog_sentence.append("#### 提出したソースコード")
            blog_sentence.append("``` python")

            with open(file_list[i-1], encoding='UTF-8') as f:
                py_code = f.read()
                blog_sentence.append(py_code)

            print(file_list[i-1])
            blog_sentence.append("```")
            blog_sentence.append("")

    blog_sentence.append("## 終わりに（余談）")
    print(blog_sentence)
    list_to_text(blog_sentence)


if __name__ == "__main__":
    main()
