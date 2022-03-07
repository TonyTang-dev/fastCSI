<template>
	<view class="content">
		<view class="title">
			<text class="txttitle">基本信息</text>
		</view>
		<image class="logo" src="/static/mine1.png"></image>
		<view class="showinfo">
			<text class="hintinfo">用户名：</text>
			<text class="userinfo">{{name}}</text>
		</view>
		<view class="showinfo">
			<text class="hintinfo">性 别：</text>
			<text class="userinfo">{{gender}}</text>
		</view>
		<view class="showinfo">
			<text class="hintinfo">年 龄：</text>
			<text class="userinfo">{{age}}</text>
		</view>
		<view class="showinfo">
			<text class="hintinfo">邮 箱：</text>
			<text class="userinfo">{{email}}</text>
		</view>
		<view class="showinfo">
			<text class="hintinfo">用户权限：</text>
			<text class="userinfo">{{userRoot}}</text>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				name:'',
				gender:'',
				age:'',
				email:'',
				registTime:'',
				userRoot:'普通用户',
				userPohto:''
			}
		},
		methods: {
			onLoad(){
				
			},
			onShow(){
				//外层指针this
				let _this=this
				//从本地获取用户权限
				uni.getStorage({
					key:"isManager",
					success(e){
						if(e.data.isManager){
							_this.userRoot="管理员"
						}
						else{
							_this.userRoot="普通用户"
						}
					}
				})
				//请求用户信息
				uni.request({
					url:'/api/getUserInfor',
					method:'POST',
					data:{},
					success(e) {
						//用户头像未获取
						_this.$u.toast("获取信息成功")
						_this.name=e.data.userName
						_this.age=e.data.userAge
						_this.gender=e.data.userSex
						_this.email=e.data.userEmail
						_this.userRoot=e.data.userRoot
						_this.userPhoto=e.data.regPhoto
					}
				})
			},
		},
	};
</script>

<style lang="scss" scoped>
	page{
		background-color: #ffffff;
	}
	.content {
		flex-direction: column;
		display: flex;
		align-items: center;
		align-content: center;
		width: 100%;
		height: 100%;
		.logo {				//头像
			height: 72px;
			width: 72px;
			margin-top: 60rpx;
			margin-left: auto;
			margin-right: auto;
			margin-bottom: 50rpx;
			border-radius: 5px;
			-moz-box-shadow:0 0 10px 10px #06c;
			-webkit-box-shadow:0 0 10px 10px #06c;
			box-shadow:0 0 10px 10px #06c;
		}
		
		.showinfo {			//显示信息设置
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
				height: 20px;
				background-color: #FFFFFF;
				border-radius: 3px;
				margin-top: 20px;
				font-size: 12px;
				-moz-box-shadow: inset 0 0 10px #CCC;
				 -webkit-box-shadow: inset 0 0 10px #CCC;
				 box-shadow: inset 0 0 10px #CCC;
			}
		}
		//模块标题
		.title{
			width: 100%;
			height: 50px;
			padding-left: 20px;
			font-size: 14px;
			padding-top: 18px;
			border-radius: 4px;
			display: flex;
			align-content: center;
			background-color: #2979FF;
		}
	}
</style>
