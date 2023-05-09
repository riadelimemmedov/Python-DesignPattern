"""
    Visitor is a behavioral design pattern that allows adding new behaviors to existing class hierarchy without altering any existing code.
"""

"""
    A real-life example of the visitor design pattern is in a program that manipulates different types of files, such as text files, PDF files, and image files. Each file type has its own unique structure and behavior, but we want to be able to perform the same set of operations on each file, such as compressing, encrypting, or extracting metadata.
"""

#!FileVisitor
class FileVisitor:
    def visit_text_file(self, text_file):
        pass

    def visit_pdf_file(self, pdf_file):
        pass

    def visit_image_file(self, image_file):
        pass


#!CompressVisitor
class CompressVisitor(FileVisitor):
    def visit_text_file(self, text_file):
        print(f"Compressing text file: {text_file.name}")

    def visit_pdf_file(self, pdf_file):
        print(f"Compressing PDF file: {pdf_file.name}")

    def visit_image_file(self, image_file):
        print(f"Compressing image file: {image_file.name}")


#!EncryptVisitor
class EncryptVisitor(FileVisitor):
    def visit_text_file(self, text_file):
        print(f"Encrypting text file: {text_file.name}")

    def visit_pdf_file(self, pdf_file):
        print(f"Encrypting PDF file: {pdf_file.name}")

    def visit_image_file(self, image_file):
        print(f"Encrypting image file: {image_file.name}")


#!File
class File:
    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        pass


#!TextFile
class TextFile(File):
    def accept(self, visitor):
        visitor.visit_text_file(self)


#!PdfFile
class PdfFile(File):
    def accept(self, visitor):
        visitor.visit_pdf_file(self)


#!ImageFile
class ImageFile(File):
    def accept(self, visitor):
        visitor.visit_image_file(self)


# _name_ == _main_
if __name__ == "__main__":
    files = [TextFile("file1.txt"), PdfFile("file2.pdf"), ImageFile("file3.png")]
    compress_visitor = CompressVisitor()
    encrypt_visitor = EncryptVisitor()

    for file in files:
        file.accept(compress_visitor)
        file.accept(encrypt_visitor)