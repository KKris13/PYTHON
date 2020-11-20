import requests
import time

class my_hhu:
    account = "1908080229"  # 学号
    password = "150015"  # 信息门户密码
    wid = "A335B048C8456F75E0538101600A6A04"  # 个人wid
    home_url = "http://my.hhu.edu.cn/index.portal"
    login_url = "http://ids.hhu.edu.cn/amserver/UI/Login"
    daka_url = "http://form.hhu.edu.cn/pdc/form/list"
    daka_list_url = "http://form.hhu.edu.cn/pdc/formDesignApi/S/gUTwwojq"
    daka_save_url = "http://form.hhu.edu.cn/pdc/formDesignApi/dataFormSave?wid=" + wid + "&userId=" + account
    init_form_api = "http://form.hhu.edu.cn/pdc/formDesignApi/initFormAppInfo"

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4209.2 Safari/537.36'
        }
        self.session = requests.Session()

    def login(self):
        post_data = {
            "Login.Token1": self.account,
            'Login.Token2': self.password,
            'goto': "http://my.hhu.edu.cn/loginSuccess.portal",
            'gotoOnFail': "http://my.hhu.edu.cn/loginFailure.portal",
        }
        loginResponse = self.session.post(self.login_url, data=post_data, headers=self.headers)
        if "handleLoginSuccessed()" in loginResponse.text:
            print("登录成功！")
        else:
            print("登录失败，请检查账号密码是否填写正确！")

    def daka(self):
        while True:
            curr_date = time.strftime('%Y/%m/%d', time.localtime(time.time()))
            self.session.get(self.daka_url)
            self.session.get(self.daka_list_url)
            post_data = {
                'DATETIME_CYCLE': curr_date,
                'XGH_336526': self.account,
                ### 此部分必须和健康打卡系统完全相同
                'XM_1474': '冯浩均',  # 姓名
                'SFZJH_859173': '445323200109150015',  # 身份证号
                'SELECT_941320': '商学院',  # 学院
                'SELECT_459666': '2019级',  # 年级
                'SELECT_814855': '信息',  # 专业
                'SELECT_525884': '信息19_2',  # 班级
                'SELECT_125597': '江宁校区教学区25舍',  # 宿舍楼
                'TEXT_950231': '929',  # 宿舍号
                'TEXT_937296': '18360851989',  # 手机号码
                ### 以下全部安按照健康算，不用修改
                'RADIO_853789': '否',
                'RADIO_43840': '否',
                'RADIO_579935': '健康',
                'RADIO_138407': '是',
            }
            self.session.post(self.init_form_api, data={'selfFormWid': self.wid}, headers=self.headers)
            dakaResponse = self.session.post(self.daka_save_url, data=post_data, headers=self.headers)
            if '{"result":true}' in dakaResponse.text:
                print("打卡成功！")
                break
            else:
                time.sleep(0.5)


if __name__ == '__main__':
    user = my_hhu()
    user.login()
    user.daka()
