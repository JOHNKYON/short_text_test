# short_text_test
Some test of short text demos

lsi函数模块已完成，进入调参生成bucket阶段。目前希望达到的效果是

某一查询进入，立即返回一个bucket，此bucket中有所有相近专业（阈值待调参）

模块化程度过高的代价是不停的传参，可能造成性能下降。不过估计这个很久才会跑一次，所以可以接受这一代价