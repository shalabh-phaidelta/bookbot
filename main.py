from enum import Enum

class REPORT_SECTIONS(Enum):
    HEADER = 1
    FOOTER = 2
    BODY = 3

class Report:
    header: str =""
    footer: str =""
    body: str   =""

    def __repr__(self):
        return f"{Report.header}\n {Report.body}\n {Report.footer}"

def main():
    book_path = "./books/frankenstein.txt"
    content = read_book(book_path)
    count = count_words(content)
    body = f"{count} num of words found in document \n\n" 
    
    ########################################

    char_count = count_chars(content)
    # body += f"{char_count} in {book_path.split('/')[-1]}"
    body += char_count

    ############################
    # print(body)
    rpt = Report()
    formatted_rpt = format_report(rpt, body)
    print(formatted_rpt)

def read_book(path: str) -> str:
    with open(path, "+r") as f:
        file_content = f.read()
    return file_content

def count_words(words: str) -> int:
    all_words = words.split()
    count  = 0;
    for w in all_words:
        count += 1
    return count

def count_chars(text: str) -> str:
    text = text.lower().strip()
    count_dict = {ch:text.count(ch) for ch in set(text)}
    val = ""
    for k,v in count_dict.items():
        val += f"The {k} character was found {v} times.\n"
    return val

def format_report(report: Report, body: str) -> str:
    report.header = "--- Begin report of books/frankenstein.txt ---\n\n"
    report.footer = "\n\n --- End of report ---\n"
    report.body = body
    final_report = f"{report.header} {report.body} {report.footer}"
    return final_report    



if __name__ == "__main__":
    main()

    ############################
    # print(count_chars("asdsadvn xyz"))
    # rpt = Report()
    # body = "abcd is the rpt"
    # fomratted_rpt = format_report(rpt, body)
    # print(fomratted_rpt)