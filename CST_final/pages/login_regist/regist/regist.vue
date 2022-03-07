<template>
	<view class="content">
		<view class="title">用户注册</view>
		<view class="inputname">
			<text class="hintinfo">用户名：</text>
			<input class="userinfo" @input="txtname" type="text" v-model="userName"  placeholder="请输入用户名" />
		</view>
		<view class="inputname">
			<text class="hintinfo">用户权限：</text>
			<input class="userinfo" @input="txtname" type="text" v-model="userRootKey"  placeholder="输入密钥成为管理员,非管理员不填" />
		</view>
		<view class="inputname">
			<text class="hintinfo">密   码：</text>
			<input class="userinfo" @input="txtpassword" type="password" v-model="userPassword" placeholder="请输入密码" />
		</view>
		<view class="inputname">
			<text class="hintinfo">确认密码：</text>
			<input class="userinfo" @input="txtPpassword" type="text" v-model="userPpassword"  placeholder="请确认密码" />
		</view>
		<view class="inputname">
			<text class="hintinfo">性 别：</text>
			<!-- 下拉菜单 -->
			<view class="pullDownMenu">
				<text class="userinfo">{{userGender}}</text>
				<picker class="pullEntry" @change="genderChange" :range="genderList">
					<label><image class="pullIcon" src="/static/pullDown.png"></image></label>
					<label class="">{{genderList[index]}}</label>
				</picker>
			</view>
		</view>
		<view class="inputname">
			<text class="hintinfo">年 龄：</text>
			<input class="userinfo" @input="txtage" type="text" v-model="userAge"  placeholder="请输入年龄" />
		</view>
		<view class="inputname">
			<text class="hintinfo">邮 箱：</text>
			<input class="userinfo" @input="txtemail" type="text" v-model="userEmail" placeholder="请输入邮箱" />
		</view>
		<view class="buttonSet">
			<u-button @click="registButton" :style="[buttonStyle]" class="button-LogReg">注册</u-button>
			<u-button @click="cancelButton" :style="[buttonStyle]" class="button-LogReg">取消</u-button>
		</view>
	</view>
</template>

<script>
	//导入md5加密包
	import w_md5 from "../../../js_sdk/zww-md5/w_md5.js"
	export default {
		data() {
			return {
				userName:'',					//用户名
				userRootKey:'',					//用户权限密钥
				userAge:'',						//用户年龄
				userEmail:'',					//用户邮箱
				userGender:'',					//用户性别
				userPassword:'',				//用户密码
				userPpassword:'',				//用户第二次去人密码
				genderList:["男","女"],			//用户性别列表
				index:-1,						//下拉索引
			}
		},
		
		//按钮风格
		computed: {
			buttonStyle() {
				let style = {};
				style.color = "#fff";
				style.backgroundColor = this.$u.color['warning'];
				return style;
			},
		},
		
		//md5加密
		components: {
			w_md5
		},
		methods: {
			onLoad(){
				
			},
			//用户权限选择下拉框
			genderChange(e){
				this.userGender=this.genderList[e.target.value];
			},
			
			//点击取消按钮
			cancelButton(){
				console.log("取消注册并返回登陆界面")
				uni.redirectTo({
					url:"../login/login",
				})
			},
			
			//注册按钮
			registButton(){
				//前期判断信息是否完善和密码是否一致
				if(this.userName==""||this.userPassword==""||this.userPpassword==""||this.userAge==""||this.userGender==""||this.userEmail==""){
					this.$u.toast("请完善信息后再点击注册")
					return
				}
				if(this.userPassword!=this.userPpassword){
					this.$u.toast("您的密码前后不一致")
					return
				}
				
				//邮箱检测格式是否符合要求//正则表达校验，邮箱格式
				var reg = /^(\w)+(\.\w+)*@(\w)+((\.\w{2,3}){1,3})$/;
				if(!reg.test(this.userEmail)){
					this.$u.toast("您的邮箱格式不符合要求,请检查")
					return
				}
				
				//检验密码位数是否符合要求
				if(this.userPassword.length!=6){
					this.$u.toast("您的密码格式不正确，请输入6位密码");
					return;
				}
				
				//this指针
				var _this=this
				
				var temptime=getTime()
				uni.showModal({
					title: '确认注册',
					content: '确认注册信息无误并提交？',
					success: function (res) {
						if (res.confirm) {
							console.log(temptime+'用户点击确定'+_this.userPassword);
							uni.request({
								url: '/api/createUser', 
								method:'POST',
								//密码为加密代码
								data:{userName:_this.userName,userRootKey:_this.userRootKey,password:w_md5.hex_md5_16(_this.userPassword),regAge:_this.userAge,regSex:_this.userGender,regEmail:_this.userEmail,regTime:temptime}, 
								success: (res) => {
									console.log(res.data);
									this.text = 'request success';
								}
							});
						} else if (res.cancel) {
							console.log('取消注册');
						}
					}
				});
			},
		},
	};
	
	//获取当前时间
	function getTime(){
		var date = new Date(),
		year = date.getFullYear(),
		month = date.getMonth() + 1,
		day = date.getDate(),
		hour = date.getHours() < 10 ? "0" + date.getHours() : date.getHours(),
		minute = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes(),
		second = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
		month >= 1 && month <= 9 ? (month = "0" + month) : "";
		day >= 0 && day <= 9 ? (day = "0" + day) : "";
		var timer = year + ',' + month + ',' + day + ',' + hour + ',' + minute + ',' + second;
		return timer;
	};
</script>

<style lang="scss" scoped>
	page{
		background-color: #f0f0f0;
	}
	.content {
		flex-direction: column;
		display: flex;
		align-items: center;
		align-content: center;
		width: 100%;
		height: 100%;
		//按钮父容器
		.buttonSet{
			flex-direction: row;
			display: flex;
		}
		.inputname {
			width: 80%;
			flex-direction: row;
			display: flex;
			//提示内容
			.hintinfo{
				width: 20%;
				margin-top: 20px;
				font-size: 12px;
			}
			
			//输入内容
			.userinfo{
				width: 70%;
				background-color: #FFFFFF;
				border-radius: 3px;
				margin-top: 20px;
				font-size: 12px;
				-moz-box-shadow: inset 0 0 10px #CCC;
				-webkit-box-shadow: inset 0 0 10px #CCC;
				box-shadow: inset 0 0 10px #CCC;
			}
		}
		
		//下拉菜单父付组件
		.pullDownMenu{
			width: 80%;
			flex-direction: row;
			display: flex;
		}
		//下拉菜单点击入口
		.pullEntry{
			margin-top: 20px;
			width: 20px;
			height: 20px;
		}
		//下拉图标
		.pullIcon{
			border-radius: 5px;
			height: 20px;
			width: 20px;
			-moz-box-shadow: inset 0 0 10px #CCC;
			-webkit-box-shadow: inset 0 0 10px #CCC;
			box-shadow: inset 0 0 10px #CCC;
		}
		
		//注册-取消按钮
		.button-LogReg{
			width: 40%;
			height: 35px;
			font-size:14px;
			margin-top: 60px;
		}
		//用户注册标题
		.title {
			margin-top: 100upx;
			text-align: center;
			font-size: 28px;
			font-weight: 500;
			margin-bottom: 100upx;
		}
		//输入框设置
		input {
			text-align: left;
			margin-bottom: 5rpx;
			padding-bottom: 6rpx;
		}
	}
</style>
