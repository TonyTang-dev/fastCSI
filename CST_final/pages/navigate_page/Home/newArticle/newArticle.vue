<template>
	<view class="content">
		<view class="title">
			<text class="txttitle">新增文章</text>
		</view>
		<view class="Title-Content">
			<text class="hintInfo">文章标题：</text>
			<textarea class="textTitle" label="文章标题:" maxlength="30" v-model="contentTitle" placeholder="请输入文章标题" auto-height="true" placeholder-style="font-size:12px;"></textarea>
		</view>
		<view class="Title-Content">
			<text class="hintInfo">文章内容：</text>
			<textarea class="textArea" :style="{height: screenHeight+'px'}" v-model="contentArea" maxlength="-1" placeholder="请输入文章内容" placeholder-style="font-size:12px;"></textarea>
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
				textAreaTitle:'文章内容:',
				userName:'',
				contentTitle:'',
				contentArea:'',
				screenHeight:'',
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
				var _this=this;
				
				//获取屏幕高度
				uni.getSystemInfo({
					success:(res)=> {
						_this.screenHeight=res.windowHeight-100;
					}
				})
			},
			onShow(){
				
			},
			
			//提交文章
			submit(){
				//外层指针this
				let _this=this
				//判断输入状态
				if(_this.contentArea==""||_this.contentTitle==""){
					_this.$u.toast("请完善文章内容再提交");
					return;
				}
				
				//提交确认
				uni.showModal({
					title: '确认提交',
					content: '确认要提交新文章吗？',
					success: function (res) {
						if (res.confirm){
							
							//获取用户名缓存
							uni.getStorage({
								key:'userInfo',
								success(e){
									_this.userName=e.data.name;
								}
							})
							//确认按钮
							_this.$u.toast('用户点击确定');
							//发送请求
							uni.request({
								url:'/api/postArticle',
								method:'POST',
								data:{userName:_this.userName,postTitle:_this.contentTitle,postText:_this.contentArea,postTime:getTime()}, 
								success: (res) => {
									console.log(res.data);
									if(res.data.data.status==true){
										_this.$u.toast("发布成功")
									}
									else{
										_this.$u.toast("发布失败")
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
					content: '确认要取消并删除草稿吗？',
					success: function (res) {
						if (res.confirm){
							//确认按钮
							uni.redirectTo({
								url:'../mySettings'
							})
						}
					}
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
		background-color: #ffffff;
	}
	.content {
		flex-direction: column;
		display: flex;
		align-items: center;
		align-content: center;
		width: 100%;
		height: 100%;
		
		//文本输入域
		.textArea{
			background-color: #f0f0f0;
			width: 90%;
			text-align: left;
			font-size:12px;
			margin-top: 10px;
			padding: 6px;
			border-radius: 8px;
			-moz-box-shadow: inset 0 0 10px #CCC;
			-webkit-box-shadow: inset 0 0 10px #CCC;
			box-shadow: inset 0 0 10px #CCC;
			// height: 100%;
		}
		//标题输入
		.textTitle{
			background-color: #f0f0f0;
			width: 90%;
			font-size:12px;
			text-align: left;
			margin-top: 10px;
			padding: 5px;
			border-radius: 8px;
			-moz-box-shadow: inset 0 0 10px #CCC;
			-webkit-box-shadow: inset 0 0 10px #CCC;
			box-shadow: inset 0 0 10px #CCC;
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
		//标题
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
		//输入框父容器
		.Title-Content{
			width: 90%;
			height: 100%;
			flex-direction: row;
			display: flex;
		}
		//提示内容的字体设置
		.hintInfo{
			font-size: 12px;
			width: 70px;
			margin-top: 10px;
		}
	}
</style>
