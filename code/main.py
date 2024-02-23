import PyQt6.QtWidgets as qtw


def main():
    """
    Main function
    :return:
    :rtype:
    """
    app = qtw.QApplication([])
    window = qtw.QWidget()
    window.setWindowTitle('Hello, World!')
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
