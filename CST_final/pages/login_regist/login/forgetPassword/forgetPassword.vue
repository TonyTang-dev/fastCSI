<template>
	<view class="content">
		<view class="title">忘记密码</view>
		<view class="inputcomponent">
			<text class="hintinfo">用户名：</text>
			<input class="userinfo" @input="txtname" type="text" v-model="userN"  placeholder="请输入用户名" />
		</view>
		<view class="inputcomponent">
			<text class="hintinfo">邮 箱：</text>
			<input class="userinfo" @input="txtemail" type="text" v-model="userEmail" placeholder="请输入邮箱" />
		</view>
		<view class="inputcomponent">
			<text class="hintinfo">新密码：</text>
			<input class="userinfo" @input="txtNewPassword" type="password" v-model="newPassword" placeholder="请输入新密码" />
		</view>
		<view class="inputcomponent">
			<text class="hintinfo">确认密码：</text>
			<input class="userinfo" @input="txtRepeatPassword" type="text" v-model="repeatNewPassword"  placeholder="请再次输入" />
		</view>
		<view class="buttonSet">
			<u-button @click="queryButton" :style="[buttonStyle]" class="button-LogReg">确认</u-button>
			<u-button @click="cancelButton" :style="[buttonStyle]" class="button-LogReg">取消</u-button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				userN: '',
				userEmail:'',
				name:'',
				email:'',
				password:'',
				passwordRepeat:''
			}
		},
		computed: {
			buttonStyle() {
				let style = {};
				style.color = "#fff";
				style.backgroundColor = this.$u.color['warning'];
				return style;
			},
		},
		methods: {
			onLoad(){
				
			},
			//获取输入框信息
			txtname(e){
				this.name=e.target.value
			},
			txtemail(e){
				this.email=e.target.value
			},
			txtNewPassword(e){
				this.password=e.target.value
			},
			txtRepeatPassword(e){
				this.passwordRepeat=e.target.value
			},
			cancelButton(){
				console.log("取消注册并返回登陆界面")
				uni.redirectTo({
					url:"../login",
				})
			},
			queryButton(){
				//this指针
				var _this=this
				
				//判断输入状态
				if(this.name==""||this.email==""||this.password==""||this.passwordRepeat==""){
					this.$u.toast("请完善信息后再查询")
					return
				}
				if(this.password!=this.passwordRepeat){
					this.$u.toast("您两次输入的密码不匹配")
					return
				}
				//密码变量
				uni.showModal({
					title: '确认改密？',
					content: '确认信息无误并更改密码？',
					success: function (res) {
						if (res.confirm) {
							console.log('用户点击确定');
							uni.request({
								url: '/api/forgetPassword', 
								method:'POST',
								//密码为加密代码
								data:{userName:_this.name,userEmail:_this.email,userPassword:_this.password}, 
								success: (res) => {
									console.log(res.data);
								}
							});
						} else if (res.cancel) {
							console.log('取消改密');
							_this.$u.toast("取消改密")
						}
					}
				});
			},
		},
	};
	function getTime(){		//获取当前时间
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
	.content {		//容器
		flex-direction: column;
		display: flex;
		align-items: center;
		align-content: center;
		width: 100%;
		height: 100%;
		.buttonSet{			//按钮
			flex-direction: row;
			display: flex;
		}
		.inputcomponent {	//输入框设置
			width: 50%;
			flex-direction: row;
			display: flex;
			.hintinfo{
				width: 50%;
				margin-top: 20px;
				font-size: 12px;
			}
			.userinfo{
				width: 60%;
				background-color: #FFFFFF;
				border-radius: 3px;
				margin-top: 20px;
				font-size: 12px;
				-moz-box-shadow: inset 0 0 10px #CCC;//阴影
				-webkit-box-shadow: inset 0 0 10px #CCC;
				box-shadow: inset 0 0 10px #CCC;
			}
		}
		.button-LogReg{
			width: 40%;
			height: 35px;
			font-size:14px;
			margin-top: 60px;
		}
		.title {
			margin-top: 100upx;
			text-align: center;
			font-size: 28px;
			font-weight: 500;
			margin-bottom: 100upx;
		}
		input {
			text-align: left;
			margin-bottom: 5rpx;
			padding-bottom: 6rpx;
		}
	}
</style>
