<template>
	<view class="content">
		<view class="button-set">
			<u-button class="button-mine" type="primary" @click="myComment">
				<image class="icon" src="/static/setting.png"></image>
				我的评论
			</u-button>
			<u-button class="button-mine"type="success" @click="myVoice">
				<image class="icon" src="/static/setting.png"></image>
				语音设置
			</u-button>
			<u-button class="button-mine"type="primary" @click="mySettings">
				<image class="icon" src="/static/setting.png"></image>
				个人设置
			</u-button>
			<u-button class="button-mine" type="warning" @click="userManage" v-show="true">
				<image class="icon" src="/static/setting.png"></image>
				用户管理
			</u-button>
		</view>		
		<!-- 用户管理有一个isShow参数 -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				isShow:false,
			}
		},
		methods: {
			//onLoad()
			onShow(){
				var _this=this;
				
				//决定是否显示管理员界面,缓存身份结果
				uni.getStorage({
					key:"isManager",
					success(e){
						console.log("是否是管理员："+e.data.isManager)
						if(e.data.isManager){
							_this.isShow=true
						}
						else{
							
						}
					}
				})
			},
			
			//我的评论按钮
			myComment(){
				uni.navigateTo({
					url:'myComment/myComment'
				})
			},
			
			//语音设置按钮
			myVoice(){
				uni.navigateTo({
					url:'myVoice/myVoice'
				})
			},
			
			//我的设置按钮
			mySettings(){
				uni.navigateTo({
					url:'mySettings/mySettings'
				})
			},
			
			//用户管理按钮
			userManage(){
				uni.navigateTo({
					url:'userManage/userManage'
				})
			}
		}
	}
</script>

<style>
	//父容器
	.content{
		width: 100%;
		flex-direction: column;
		display: flex;
		align-items: center;
	}
	
	//按钮集合
	.button-set{
		width: 80%;
		margin-top: 5px;
	}
	.button-mine{
		width: 100%;
		font-size:12px;
		margin-top: 3px;
		height: 30px;
	}
	
	//图标
	.icon{
		width: 20px;
		height: 20px;
		margin-right: 20px;
		border-radius: 3px;
		-moz-box-shadow:0 0 1px 1px #06c;
		-webkit-box-shadow:0 0 1px 1px #06c;
		box-shadow:0 0 1px 1px #06c;
	}
</style>
