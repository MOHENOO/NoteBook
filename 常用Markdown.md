# 常用Markdown

# *斜体* **粗体**

# 一级标题

## 二级标题

### 三级标题

[链接](www.baidu.com)

+ 列表

  1. 列表二

     > 引用

  `行内代码:Hello World!`

  ​    这是一个代码块，此行左侧有四个不可见的空格。
代码块前后需要有至少一个空行，且每行代码前需要有至少一个 Tab 或四个空格；

		代码块：int main()
		{
		return 0;
		}//typore 不支持代码块

![图片](/home/mohenoo/Public/Pictures/1.png)

[TOC]

Tags: Markdown //typora simplenote不支持标签

~~删除线~~

$行内公式 E=mc^2$

$$整行公式$$

```c
int main()
{
    return 0;//语法高亮代码
}
```



```flow
st=>start: Start:>https://www.zybuluo.com
io=>inputoutput: verification
op=>operation: Your Operation
cond=>condition: Yes or No?
sub=>subroutine: Your Subroutine
e=>end

st->io->op->cond
cond(yes)->e
cond(no)->sub->io
```
| 项目 | 价格 | 数量 |
| ---- | ---: |:--: |
| 计算机 | \$1600 |  5   |
| 手机   |   \$12 |  12  |
| 管线   |    \$1 | 234  |

- [ ] 代办事项
