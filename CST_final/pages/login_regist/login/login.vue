<template>
	<view class="content">
		<view class="title">CSI技术语音吧</view>
		<image class="logo" :src="myHeadPhoto"></image>
		<view class="inputname">
			<text class="hintName">用户名：</text>
			<input class="userName" type="text" v-model="userName"  placeholder="请输入用户名" />
		</view>
		<view class="inputname">
			<text class="hintPassword">密   码：</text>
			<input class="userPassword" type="password" v-model="userPassword" placeholder="请输入密码" />
		</view>
		<view class="aboutpassword">
			<u-checkbox class="checkbox" size="13px" icon-size="12px" label-size="12px" @change="checkboxChange" v-model="checked" :disabled="false">记住密码</u-checkbox>
			<text class="forget" @click="forgetpassword">忘记密码？</text>
		</view>
		<view class="buttonSet">
			<u-button @click="submit" :style="[buttonStyle]" class="button-LogReg">登录</u-button>
			<u-button @click="registButton" :style="[buttonStyle]" class="button-LogReg">注册</u-button>
		</view>
	</view>
</template>

<script>
	//导入md5加密包
	import w_md5 from "../../../js_sdk/zww-md5/w_md5.js"
	export default {
		data() {
			return {
				checked: false,
				userName: '',
				userPassword:'',
				name:'',
				password:'',
				myHeadPhoto:'',
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
		//md5加密
		components: {
			w_md5
		},
		methods: {
			onLoad(){
				var _this=this
				_this.$u.toast("头像加载"),
				
				//获取网络状态
				uni.getNetworkType({
					success(res) {
						if(res.networkType=="none"){
							_this.$u.toast("您当前处于无网络状态，无法正常启动")
						}
						else if(res.networkType=="unknown"){
							_this.$u.toast("您处于未知网络环境中");
						}
						else{
							_this.$u.toast("您处于网络环境中");
						}
					},
					fail(e) {
						_this.$u.toast("无法获取您的网络状态");
					},
				});
				
				//头像加载
				uni.getStorage({
					key:"headPhotoLink",
					success(e){
						if(e.data.Photolink!=""){
							_this.myHeadPhoto=e.data.Photolink
						}
						else{
							_this.myHeadPhoto="/static/mine1.png"
							// _this.$u.toast("头像加载失败")
						}
					},
					fail(e){
						_this.myHeadPhoto="/static/mine1.png"
						// _this.$u.toast("头像加载失败")
					}
				})
			},
			onShow(){
				//this指针
				var _this=this
				
				//打开页面则判断是否显示密码
				uni.getStorage({
					key:"userInfo",
					success(e){
						console.log("记住密码："+e.data.ischecked+" 密码："+e.data.password)
						if(e.data.ischecked){
							_this.checked=e.data.ischecked
							_this.userName=e.data.name
							_this.userPassword=e.data.password
						}
						else{
							_this.userName='';
							_this.userPassword='';
						}
					}
				})
			},
			// 选中复选框时，由checkbox时触发
			checkboxChange(e) {
				this.checked=e.value
			},
			
			//忘记密码
			forgetpassword(){
				uni.navigateTo({
					url:'forgetPassword/forgetPassword'
				})
			},
			
			//登录
			submit() {
				//this指针
				var _this=this;
				
				//获取本地时间
				var temptime=getTime()
				console.log("本地时间"+temptime)
				
				//判断状态
				if(_this.userName=="" || _this.userPassword==""){
					this.$u.toast("请先完善用户名和密码再登录")
					return
				}
				
				// //检验密码位数是否符合要求
				// if(this.password.length!=6){
				// 	this.$u.toast("您的密码格式不正确，请输入6位密码");
				// 	return;
				// }
				
				if(_this.checked==true){
					console.log("记住密码,md5加密");
					//缓存用户名密码
					uni.setStorage({
						key:"userInfo",
						//md5加密密码
						data:{name:_this.userName,password:_this.userPassword,ischecked:_this.checked}
					})
				}
				else{
					//清除缓存
					uni.removeStorage({
						key:"userInfo",
						success() {
							console.log("缓存信息已删除")
						}
					})
				}
				this.$u.toast('发出登录请求')
				//输出显示验证
				console.log("\nname:"+_this.userName+"\n加密password:"+_this.userPassword)
				uni.switchTab({
					// url:"../../navigate_page/Home/home"
					url:"../../navigate_page/Home/home"
				})
				uni.request({
					url: '/api/login', 
					
					//fastmock模拟服务器发送信息
					// url:"https://www.fastmock.site/mock/9d37f7101ed004047c072cfd4be77eae/api/api/login",
					method:'POST',
					data:{userName:_this.userName,password:_this.userPassword,loginTime:temptime}, 
					success: (res) => {
						console.log(res.data);
						if(res.data.admin==1){
							//获取管理员权限状态
							uni.setStorage({
								key:"isManager",
								//管理员权限
								data:{isManager:true}
							})
						}
						else{
							
							//设置是否为管理员缓存
							uni.setStorage({
								key:"isManager",
								//管理员权限
								data:{isManager:false}
							})
						}
					}
				});
			},
			registButton(){
				uni.navigateTo({
					url:"../regist/regist"
				})
			}
		},
	};
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
		.buttonSet{
			flex-direction: row;
			display: flex;
		}
		.checkbox{
			margin-top: 20px;
		}
		.logo {
			height: 72px;
			width: 72px;
			margin-top: 30rpx;
			margin-left: auto;
			margin-right: auto;
			margin-bottom: 50rpx;
			border-radius: 5px;
			-moz-box-shadow:0 0 10px 10px #06c;
			-webkit-box-shadow:0 0 10px 10px #06c;
			box-shadow:0 0 10px 10px #06c;
		}
		.inputname {
			width: 50%;
			flex-direction: row;
			display: flex;
			.hintName{
				width: 70px;
				font-size: 12px;
				flex-direction: row;
				display:flex;
				align-items: center;
			}
			.hintPassword{
				width: 70px;
				margin-top: 20px;
				flex-direction: row;
				display:flex;
				align-items: center;
				font-size: 12px;
			}
			.userName{
				width: 100%;
				border-radius: 3px;
				background-color: #FFFFFF;
				font-size: 11px;
				-moz-box-shadow: inset 0 0 10px #CCC;
				-webkit-box-shadow: inset 0 0 10px #CCC;
				box-shadow: inset 0 0 10px #CCC;
			}
			.userPassword{
				width: 100%;
				background-color: #FFFFFF;
				border-radius: 3px;
				margin-top: 20px;
				font-size: 11px;
				-moz-box-shadow: inset 0 0 10px #CCC;
				-webkit-box-shadow: inset 0 0 10px #CCC;
				box-shadow: inset 0 0 10px #CCC;
			}
		}
		.forget{
			font-size: 12px;
			margin-left: 40px;
			margin-top: 20px;
			color: #2B85E4;
		}
		.button-LogReg{
			width: 40%;
			height: 35px;
			font-size: 14px;
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
			margin-bottom: 10rpx;
			padding-bottom: 6rpx;
		}
	}
</style>
