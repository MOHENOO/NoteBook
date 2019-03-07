# 一个Web服务器

该程序其实只是个Web服务器的重用。 Google在http://chart.apis.google.com 上提供了一个将表单数据自动转换为图表的服务。不过，该服务很难交互，因为你需要将数据作为查询放到URL中。此程序为一种数据格式提供了更好的的接口：给定一小段文本，它将调用图表服务器来生成二维码（QR码），这是一种编码文本的点格矩阵。该图像可被你的手机摄像头捕获，并解释为一个字符串，比如URL，这样就免去了你在狭小的手机键盘上键入URL的麻烦。

以下为完整的程序，随后有一段解释。

```go
package main

import (
    "flag"
    "html/template"
    "log"
    "net/http"
)

var addr = flag.String("addr", ":1718", "http service address") // Q=17, R=18

var templ = template.Must(template.New("qr").Parse(templateStr))

func main() {
    flag.Parse()
    http.Handle("/", http.HandlerFunc(QR))
    err := http.ListenAndServe(*addr, nil)
    if err != nil {
        log.Fatal("ListenAndServe:", err)
    }
}

func QR(w http.ResponseWriter, req *http.Request) {
    templ.Execute(w, req.FormValue("s"))
}

const templateStr = `
<html>
<head>
<title>QR Link Generator</title>
</head>
<body>
{{if .}}
<img src="http://chart.apis.google.com/chart?chs=300x300&cht=qr&choe=UTF-8&chl={{.}}" />
<br>
{{.}}
<br>
<br>
{{end}}
<form action="/" name=f method="GET"><input maxLength=1024 size=70
name=s value="" title="Text to QR Encode"><input type=submit
value="Show QR" name=qr>
</form>
</body>
</html>
`
```

main之前的代码应该比较容易理解。我们通过一个标志为服务器设置了默认端口。模板变量templ正式有趣的地方。它构建的HTML模版将会被服务器执行并显示在页面中。稍后我们将详细讨论。

main函数解析了参数标志并使用我们讨论过的机制将QR函数绑定到服务器的根路径。然后调用http.ListenAndServe启动服务器；它将在服务器运行时处于阻塞状态。

QR仅接受包含表单数据的请求，并为表单值s中的数据执行模板。

模板包 html/template 非常强大；该程序只是浅尝辄止。本质上，它通过在运行时将数据项中提取的元素（在这里是表单值）传给templ.Execute执行因而重写了HTML文本。在模板文本（templateStr）中，双大括号界定的文本表示模板的动作。从{{if.}}到{{end}}的代码段仅在当前数据项（这里是点.）的值非空时才会执行。也就是说，当字符串为空时，此部分模板段会被忽略。

其中两段{{.}}表示要将数据显示在模板中（即将查询字符串显示在Web页面上）。HTML模板包将自动对文本进行转义，因此文本的显示是安全的。

余下的模板字符串只是页面加载时将要显示的HTML。如果这段解释你无法理解，请参考文档获得更多有关模板包的解释。