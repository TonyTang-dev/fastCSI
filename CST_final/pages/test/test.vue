<template>
	<view class="content">
		<view class="title">
			<text class="txttitle">语音设置</text>
		</view>
		<view class="showinfo">
			<text class="hintinfo">性 别：</text>
			<view class="pullDownMenu">
				<text class="userinfo">{{gender}}</text>
				<!-- 下拉菜单 -->
				<picker class="pullEntry" @change="genderChange" :range="genderList">
					<label><u-icon class="pullIcon" name="/static/pullDown.png"></u-icon></label>
					<label class="">{{genderList[index]}}</label>
				</picker>
			</view>
		</view>
		<view class="showinfo">
			<text class="hintinfo">语速：</text>
			<!-- 下拉菜单 -->
			<view class="pullDownMenu">
				<text class="userinfo">{{speed}}</text>
				<picker class="pullEntry" @change="speedChange" :range="rootList">
					<label><u-icon class="pullIcon" name="/static/pullDown.png"></u-icon></label>
					<label class="">{{rootList[index]}}</label>
				</picker>
			</view>
		</view>
		<view class="showinfo">
			<text class="hintinfo">音量：</text>
			<!-- 下拉菜单 -->
			<view class="pullDownMenu">
				<text class="userinfo">{{volume}}</text>
				<picker class="pullEntry" @change="volumeChange" :range="rootList">
					<label><u-icon class="pullIcon" name="/static/pullDown.png"></u-icon></label>
					<label class="">{{rootList[index]}}</label>
				</picker>
			</view>
		</view>
		<view class="showinfo">
			<text class="hintinfo">音调：</text>
			<!-- 下拉菜单 -->
			<view class="pullDownMenu">
				<text class="userinfo">{{tone}}</text>
				<picker class="pullEntry" @change="toneChange" :range="rootList">
					<label><u-icon class="pullIcon" name="/static/pullDown.png"></u-icon></label>
					<label class="">{{rootList[index]}}</label>
				</picker>
			</view>
		</view>
		<view class="buttonSet">
			<u-button @click="submit" :style="[buttonStyle]" class="button-LogCancel">提交</u-button>
			<u-button @click="cancel" :style="[buttonStyle]" class="button-LogCancel">取消</u-button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				genderList:["男","女"],			//用户性别列表
				rootList:["1","2","3","4","5"],	//用户语音设置登记列表
				gender:'男',					//用户性别
				speed:'1',						//用户发声风格
				volume:'1',						//用户设置音量
				tone:'1',						//用户设置音调
				index:-1,						//默认选中下标
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
		methods: {
			onLoad(){
				
			},
			
			//性别选择下拉框
			genderChange: function(e) {
				this.gender=this.genderList[e.target.value];
			},
			//用户音量选择下拉框
			volumeChange(e){
				this.volume=this.rootList[e.target.value];
			},
			//用户音速选择下拉框
			volumeChange(e){
				this.speed=this.rootList[e.target.value];
			},
			//用户音调选择下拉框
			toneChange(e){
				this.tone=this.rootList[e.target.value];
			},
			
			// onShow(){
			// 	//外层指针this
			// 	let _this=this
			// 	//从本地获取用户权限
			// 	uni.getStorage({
			// 		key:"isManager",
			// 		success(e){
			// 			if(e.data.isManager){
			// 				_this.userRoot="管理员"
			// 			}
			// 			else{
			// 				_this.userRoot="普通用户"
			// 			}
			// 		}
			// 	})
			// 	//请求用户信息
			// 	uni.request({
			// 		url:'/api/getUserInfor',
			// 		method:'POST',
			// 		data:{},
			// 		success(e) {
			// 			//用户头像未获取
			// 			_this.$u.toast("获取信息成功")
			// 			_this.name=e.data.userName
			// 			_this.age=e.data.userAge
			// 			_this.gender=e.data.userSex
			// 			_this.email=e.data.userEmail
			// 			_this.userRoot=e.data.userRoot
			// 			_this.userPhoto=e.data.regPhoto
			// 		}
			// 	})
			// },
			
			//确认修改语音信息
			submit(){
				//外层指针this
				let _this=this
				
				//提交确认
				uni.showModal({
					title: '确认提交',
					content: '确认要更改语音设置吗？',
					success: function (res) {
						if (res.confirm){
							//确认按钮
							_this.$u.toast('用户点击确定');
							//发送请求
							uni.request({
								url:'/api/voiceSettings',
								method:'POST',
								data:{speed:this.speed,volume:this.volume,tone:this.tone,gender:this.gender}, 
								success: (res) => {
									console.log(res.data);
									if(res.data.data.status==true){
										_this.$u.toast("修改成功")
										uni.redirectTo({
											url:'../navigate_page/mine/mine',
										})
									}
									else{
										_this.$u.toast("发布失败,请重新提交")
									}
								}
							});
						} else if (res.cancel) {
							_this.$u.toast('取消上传');
						}
					}
				});
			},
			//取消上传文章
			cancel(){
				uni.showModal({
					title: '确认取消',
					content: '确认要取消并推出编辑吗？',
					success: function (res) {
						if (res.confirm){
							//确认按钮
							uni.redirectTo({
								url:'../navigate_page/mine/mine'
							})
						}
					}
				})
			}
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
				width: 80%;
				height: 20px;
				background-color: #FFFFFF;
				border-radius: 3px;
				margin-top: 20px;
				font-size: 12px;
				-moz-box-shadow: inset 0 0 10px #CCC;
				-webkit-box-shadow: inset 0 0 10px #CCC;
				box-shadow: inset 0 0 10px #CCC;
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
				height: 20px;
				width: 20px;
			}
		}
		
		//提交和取消按钮
		.buttonSet{
			flex-direction: row;
			display: flex;
		}
		//按钮风格
		.button-LogCancel{
			width: 40%;
			height: 35px;
			font-size: 14px;
			margin-top: 60px;
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
