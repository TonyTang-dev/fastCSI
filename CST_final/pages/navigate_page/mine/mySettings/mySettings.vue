<template>
	<view class="content">
		<view class="title">
			<text class="txttitle">个人设置</text>
		</view>
		<view class="button-set">
			<u-button class="button-mine" type="primary" @click="myInfo">
				<image class="icon" src="/static/setting.png"></image>
				基本信息
			</u-button>
			<u-button class="button-mine"type="success" @click="modifyPassword">
				<image class="icon" src="/static/setting.png"></image>
				修改密码
			</u-button>
			<u-button class="button-mine"type="primary" @click="modifyHeadPhoto">
				<image class="icon" src="/static/setting.png"></image>
				修改头像
			</u-button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			onLoad(){
				
			},
			//按钮点击事件
			myInfo(){
				uni.navigateTo({
					url:'basicInfo/basicInfo'
				})
			},
			modifyPassword(){
				uni.navigateTo({
					url:'modifyPassword/modifyPassword'
				})
			},
			modifyHeadPhoto(){
				uni.navigateTo({
					url:'modifyPotrait/modifyPotrait'
				})
			},
		}
	}
</script>

<style>
	page{
		background-color: #f0f0f0;
	}
	.content{
		width: 100%;
		flex-direction: column;
		display: flex;
		align-items: center;
		}
		
		//按钮
		.button-set{
			width: 90%;
			flex-direction: column;
			display: flex;
			align-items: center;
		}
		.button-mine{
			width: 100%;
			font-size:12px;
			margin-top: 3px;
			height: 30px;
		}
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
		//图标
		.icon{
			width: 20px;
			height: 20px;
			margin-right: 20px;
			border-radius: 3px;
			-moz-box-shadow:0 0 1px 1px #ff5500;
			-webkit-box-shadow:0 0 1px 1px #ff5500;
			box-shadow:0 0 1px 1px #ff5500;
		}
			input {
				text-align: left;
				margin-bottom: 5rpx;
				padding-bottom: 6rpx;
			}
</style>
