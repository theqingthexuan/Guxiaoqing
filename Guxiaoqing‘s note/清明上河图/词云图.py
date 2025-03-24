from wordcloud import WordCloud
import imageio


mk=imageio.imread_v2("qy_sty.png")
wcd=WordCloud(background_color="white",font_path="STXINGKA.TTF",mask=mk,contour_color='red',contour_width=10,repeat=True,max_words=200)
#wcd=WordCloud(background_color="white",font_path="STXINGKA.TTF",repeat=True,max_words=200)
text=" 清远丝苗米  英德红茶 西牛麻竹笋 连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡  连州菜心  清远鸡 "
wcd.generate(text)
wcd.to_file("1.png")
