# ChineseWordsNumberInPDF

## 依赖
	1. python3
	2. pdfminer3k -----> pip install pdfminer3k

## 功能
	统计PDF文件中各文字类别字数

## 使用方法
	当前目录下，运行
		./wordsNumberInPDF.sh <yourPDF.pdf> <PathOfresultFile>
	结果：
		1.终端会打印出各类型符号字数
		2.在给定的目录下会生成文件，保存pdf的文本格式


## 更新
	V_1
		输出结果中中文字数为确切数字，其他数字不准确。
		### 问题
		WARNING:pdfminer.converter:undefined: <PDFType1Font: basefont='FVMBKT+txsys'>, 21



