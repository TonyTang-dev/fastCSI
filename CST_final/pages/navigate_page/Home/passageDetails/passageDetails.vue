<template>
    <view class="content">
		
		<!-- 文章详情 -->
		<view class="title">
			<text class="txttitle">文章详情</text>
		</view>
		<view class="cell">
			<view class="element">
			   <image class="icon" @click="userinfoClick" src="/static/mine1.png"></image>
			   <view class="fatherVessel">
					<view class="topBar">
						<text @click="passageDetail">{{passageInfor.split(" ")[0]}}</text>
						<text @click="passageDetail">{{passageInfor.split(" ")[1]}}</text>
						<text @click="passageDetail">{{passageInfor.split(" ")[2]}}</text>
					</view>
					<view class="editBar">
						<!-- 评论时间+编辑评论 -->
						<text class="commentTime">作者注册时间:{{commentTime}}</text>
					</view>
					<view v-if="idPassage!=currentIndex" class="audioSetting">
						<image class="playIcon" @click="playAudio" src="/static/play.png" :id="idPassage"></image>
						<text class="processorText" :id="idPassage">00:00/00:00</text>
						<u-line-progress class="processorBar" :height="processorHeight" :striped="true" :percent="zero" :show-percent="false" :striped-active="true" :id="idPassage"></u-line-progress>
						<text class="likes" @click="likesClick">|赞:{{likes}}</text>
					</view>
					<view v-if="idPassage==currentIndex" class="audioSetting">
						<image class="playIcon" @click="playAudio" src="/static/pause.png" :id="idPassage"></image>
						<text class="processorText" :id="idPassage">{{currentPlayTime}}:00/{{duration}}:00</text>
						<u-line-progress class="processorBar" :height="processorHeight" :striped="true" :percent="zero" :show-percent="false" :striped-active="true" :id="idPassage"></u-line-progress>
						<text class="likes" @click="likesClick">|赞:{{likes}}</text>
					</view>
			   </view>
			</view>
		</view>
		<!-- 用此操作条操作文章-评论 -->
		<view class="opBar">
			<text class="giveComment" @click="giveCommentClick">|评论|</text>
		</view>
		<!-- 热门评论 -->
		<view class="allComment">
			<text class="titleComment">热门评论</text>
			<u-button @click="buttonDelete" class="deletebutton">删除</u-button>
		</view>
		<view class="list">
			<view class="cell" hover-class="hover" v-for="(item,index) in hotCommentList" :key="index">
				<view class="element">
				   <image class="icon" @click="userinfoClick" src="/static/mine1.png" :id="index"></image>
				   <view class="fatherVessel">
						<view class="commentBar">
							<text @click="passageDetail" :id="index">{{item.split(" ")[0]}}</text>
						</view>
						<text @click="passageDetail" :id="index">{{item.split(" ")[1]}}</text>
						<view class="editBar">
							<!-- 评论时间+编辑评论 -->
							<text class="commentTime">评论时间:{{commentTime}}</text>
						</view>
						<!-- 删除评论复选框 -->
						<view class="checkboxes" v-if="index!=currentCheckBoxIndex">
							<!-- 删除选择复选框 -->
							<u-checkbox class="checkbox" size="12px" icon-size="12px" label-size="12px" @change="hotCommentCheckboxChange" v-model="checkedHotComment[index]" :disabled="false" :v-show="showCheckboxes" :id="index">删除评论</u-checkbox>
						</view>
						<view class="checkboxes" v-if="index==currentCheckBoxIndex">
							<!-- 删除选择复选框 -->
							<u-checkbox class="checkbox" size="12px" icon-size="12px" label-size="12px" @change="hotCommentCheckboxChange" v-model="checkedHotComment[index]" :disabled="false" :v-show="showCheckboxes" :id="index">删除评论</u-checkbox>
						</view>
						<view v-if="index!=currentIndex" class="audioSetting">
							<image class="playIcon" @click="playAudio" src="/static/play.png" :id="index"></image>
							<text class="processorText" :id="index">00:00/00:00</text>
							<u-line-progress class="processorBar" :height="processorHeight" :striped="true" :percent="zero" :show-percent="false" :striped-active="true" :id="index"></u-line-progress>
							<text class="likes" @click="likesClick">|赞:{{item.split(" ")[3]}}</text>
						</view>
						<view v-if="index==currentIndex" class="audioSetting">
							<image class="playIcon" @click="playAudio" src="/static/pause.png" :id="index"></image>
							<text class="processorText" :id="index">{{currentPlayTime}}:00/{{duration}}:00</text>
							<u-line-progress class="processorBar" :height="processorHeight" :striped="true" :percent="playPercent" :show-percent="false" :striped-active="true" :id="index"></u-line-progress>
							<text class="likes" @click="likesClick">|赞:{{item.split(" ")[3]}}</text>
						</view>
				   </view>
				</view>
			</view>
		</view>
		
		<!-- 所有评论 -->
		<view class="allComment">
			<text class="titleComment">所有评论</text>
		</view>
		<view class="list">
			<view class="cell" hover-class="hover" v-for="(item,index) in allCommentList" :key="index">
				<view class="element">
				   <image class="icon" @click="userinfoClick" src="/static/mine1.png" :id="index+5"></image>
				   <view class="fatherVessel">
						<view class="commentBar">
							<text @click="passageDetail" :id="index+5">{{item.split(" ")[0]}}</text>
						</view>
						<text @click="passageDetail" :id="index+5">{{item.split(" ")[1]}}</text>
						<view class="editBar">
							<!-- 评论时间+编辑评论 -->
							<text class="commentTime">评论时间:{{commentTime}}</text>
						</view>
						<!-- 删除评论复选框 -->
						<view class="checkboxes" v-if="index!=currentCheckBoxIndex">
							<!-- 删除选择复选框 -->
							<u-checkbox class="checkbox" size="12px" icon-size="12px" label-size="12px" @change="allCommentCheckboxChange" v-model="checkedAllComment[index]" :disabled="false" :v-show="showCheckboxes" :id="index">删除评论</u-checkbox>
						</view>
						<view class="checkboxes" v-if="index==currentCheckBoxIndex">
							<!-- 删除选择复选框 -->
							<u-checkbox class="checkbox" size="12px" icon-size="12px" label-size="12px" @change="allCommentCheckboxChange" v-model="checkedAllComment[index]" :disabled="false" :v-show="showCheckboxes" :id="index">删除评论</u-checkbox>
						</view>
						<view v-if="(index+5)!=currentIndex" class="audioSetting">
							<image class="playIcon" @click="playAudio" src="/static/play.png" :id="index+5"></image>
							<text class="processorText" :id="index+5">00:00/00:00</text>
							<u-line-progress class="processorBar" :height="processorHeight" :striped="true" :percent="zero" :show-percent="false" :striped-active="true" :id="index"></u-line-progress>
							<text class="likes" @click="likesClick">|赞:{{item.split(" ")[3]}}</text>
						</view>
						<view v-if="(index+5)==currentIndex" class="audioSetting">
							<image class="playIcon" @click="playAudio" src="/static/pause.png" :id="index+5"></image>
							<text class="processorText" :id="index+5">{{currentPlayTime}}:00/{{duration}}:00</text>
							<u-line-progress class="processorBar" :height="processorHeight" :striped="true" :percent="playPercent" :show-percent="false" :striped-active="true" :id="index"></u-line-progress>
							<text class="likes" @click="likesClick">|赞:{{item.split(" ")[3]}}</text>
						</view>
				   </view>
				</view>
			</view>
		</view>
    </view>
</template>

<script>
	//全局音频播放器实例
	const audioIns = uni.createInnerAudioContext();
	
	export default {
		data() {
			return {
				passageInfor:'作者:张三 文章标题:山上的庙 发布时间：2020-07-12-12:09:31',
				likes:99,						//点赞数
				currentCheckBoxIndex:-1,		//选择复选框索引
				processorHeight:"5px",			//进度条高度
				commentTime:"2019-07-12 12:10:13",//评论时间
				currentPlayTime:"00",		//进度文本
				checkedHotComment:[false,true],	//复选框选中状态
				checkedAllComment:[true,false],	//复选框选中状态
				zero:0,							//给进度条设置的0状态
				currentIndex:-1,				//初始化列表索引下标
				idPassage:-2,					//为文章设置的特有id
				duration:0,						//音频时长
				userName:'',					//用户名
				list:["作者:张三 文章标题:山上的庙 12","作者:李四 文章标题:嘿嘿 31"],//列表值
				hotCommentList:["评论者:王五 注册时间:2020-07-12-14:03:23 评论时间:2021-06-05-23:23:12 83",
							"评论者:王五 注册时间:2020-07-12-14:03:23 评论时间:2021-06-05-23:23:12 14",],
							
												//热门评论集合
				allCommentList:["评论者:赵六 注册时间:2020-07-12-14:03:23 评论时间:2021-06-05-23:23:12 83",
							"评论者:唐山 注册时间:2020-07-12-14:03:23 评论时间:2021-06-05-23:23:12 14"],

				playStatus:false,				//播放状态，暂停/播放
				playORnot:true,					//播放状态，true/false
				playPercent:0,					//进度条
				audioSrc:'',					//播放源链接
				showCheckboxes:true,			//是否显示删除复选框
				//判断状态
				hasHotItem:false,			//用于判断是否有热门评论删除项
				hasHAllItem:false,			//用于判断是否有所有评论删除项
				
			}
		},
		onLoad(){
			//此处应访问文章详细内容
			let _this=this;
			uni.request({
				url:'',
				method:"POST",
				date:{},
				success:(res)=> {
					// _this.$u.toast("获取所有用户信息成功");
					//此处用for循环实现信息获取
					//for(var i=0;i<length;i++){
					// 
					// }
				}
			})
			// this.list.push("张四-男-22-12345678@qq.com")
		},
		methods:{
			//点击用户头像打开用户信息详情
			userinfoClick(e){
				//这里要解析出用户姓名等等以道详情页面展示
				uni.navigateTo({
					//用带参跳转
					url:'../mySettings/basicInfo/basicInfo'
				})
			},
			
			//点击删除按钮
			buttonDelete(e){
				//this指针
				let _this=this;
				
				//两层嵌套循环,判断是否有删除对象
				for(var i=0;i<_this.checkedHotComment.length;i++){
					if(_this.checkedHotComment[i]){
						_this.hasHotItem=true;
						break;
					}
				}
				for(var i=0;i<_this.checkedAllComment.length;i++){
					if(_this.checkedAllComment[i]){
						_this.hasAllItem=true;
						break;
					}
				}
				
				if(!_this.hasHotItem && !_this.hasAllItem){			//没有选择热门评论删除项则查看是否有所有评论部分删除项
					_this.$u.toast("请选择要删除的评论");
					return;
				}
				
				//弹窗确认删除此用户信息
				uni.showModal({
					title: '确认删除',
					content: '确认要删除选中评论吗？',
					success: function (res) {
						if (res.confirm) {
							_this.$u.toast('用户点击确定');
							
							//遍历列表删除对应评论
							if(_this.hasHotItem){						//热门评论部分
								var checkedListLength=_this.hotCommentList.length;
								for(var i=0,j=0;i<checkedListLength;i++){
									if(_this.checkedHotComment[j]){
										_this.hotCommentList.splice(j,1);	//删除评论内容
										_this.checkedHotComment.splice(j,1);//删除选中标识
									}
									else{
										j=j+1;
									}
								}
							}
							if(_this.hasAllItem){		//所有评论部分
								var checkedListLength=_this.allCommentList.length;
								for(var i=0,j=0;i<checkedListLength;i++){
									if(_this.checkedAllComment[j]){
										_this.allCommentList.splice(j,1);	//删除评论内容
										_this.checkedAllComment.splice(j,1);//删除选中标识
									}
									else{
										j=j+1;
									}
								}
							}
							//向服务器发送删除对象，列表形式
							// uni.request({
							// 	url:'/api/deleteUser',
							// 	method:'POST',
							// 	data:{userName:_this.userName},
							// 	success(e) {
							// 		_this.$u.toast("删除成功")
							// 		_this.list.splice(deleteid,1);
							// 	},
							// 	fail(e) {
							// 		_this.$u.toast("删除失败")
							// 	}
							// });
						} 
						else if (res.cancel) {
							_this.$u.toast('取消删除');
						}
					}
				});
			},
			
											//选择热门评论复选框以删除评论
			hotCommentCheckboxChange(e){
				var index=e.target.id;		//点击复选框所得id
				
											//通过列表去设置对应的选中状态
				this.hotCommentList[index]=!this.hotCommentList[index];//将对应状态的复选框取反
			},
			
			allCommentCheckboxChange(e){	//选择所有评论复选框以删除评论
				var index=e.target.id;		//点击复选框所得id
				
											//通过列表去设置对应的选中状态
				this.allCommentList[index]=!this.allCommentList[index];//将对应状态的复选框取反
			},
			
			//点击点赞数
			likesClick(){
				this.$u.toast("当前未安排点赞响应");
			},
			//评论文章按钮点击
			giveCommentClick(){
				uni.navigateTo({
					url:'../../mine/myComment/editComment/editComment',
				})
			},
			
			
				//播放评论音频,对热门评论和所有评论的播放要求，通过index实现对
				//热门评论的调整，index+5实现对所有评论的调整，区别开来处理
			playAudio(e){			
				//this指针
				let _this=this;
				_this.$u.toast(e.target.id);
				
				//音乐操作
				if(_this.audioSrc==''){
					audioIns.src = 'http://192.168.1.112:8000/static/audio/music.mp3';
				}
				
				//判断条件,当正在播放且点击了另外的音频，先停止当前正在播放的音乐
				if(_this.playStatus && _this.currentIndex!=e.target.id){
					//先暂停其他资源的播放
					_this.playStatus=false;
					_this.currentIndex=-1;
					_this.playORnot=true;
					audioIns.stop();
					_this.playPercent=0;
				}
				
				//点击播放
				if(_this.playORnot){
					//播放状态，设置为正在播放
					_this.playStatus=true;
					
					//获取播放id
					_this.currentIndex=e.target.id;
					
					//通过playORnot去判断下一次再点击此列表元素是否播放音频
					_this.playORnot=false;
					audioIns.play();
					audioIns.onPlay(() => {
						_this.$u.toast('开始播放');
					});
					// _this.playPercent=audioIns.currentTime;
					//获取音频时长
					audioIns.onCanplay(function(e){
						_this.duration=parseInt(audioIns.duration);
					});
					
					//获取当前播放时间
					audioIns.onTimeUpdate(function(e){
						_this.playPercent=audioIns.currentTime;
						_this.currentPlayTime=parseInt(audioIns.currentTime);
					})
				}
				
				//点击暂停
				else{
					_this.play='播放';
					_this.currentIndex=-1;
					_this.playORnot=true;
					audioIns.pause();
					_this.playPercent=0;
					audioIns.onPause(() => {
						_this.$u.toast('暂停播放');
					});
				}
				//音频播放错误时发出报告
				audioIns.onError((res) => {
				  _this.$u.toast("音频播放发生错误,加载失败");
				  _this.$u.toast(res.errCode);
				});
			},
			
			//点击作者和标题内容打开用户信息
			passageDetail(e){
				console.log(e.target.id)
				uni.navigateTo({
					url:'../../Home/passageDetails/passageDetails'
				})
			}
		}
	}
</script>

<style>
	.content{
		flex-direction: column;
		align-items: center;
		display: flex;
	}
	//一个列元素
	.cell{
		flex-direction: column;
		align-items: center;
		display: flex;
		width: 100%;
	}
	
	//在热门评论里通过list父组件设置宽度
	.list{
		width: 100%;
	}
	//列表外框-元素
	.element{
		flex-direction: row;
		display: flex;
		align-items: center;
		width: 90%;
		height: 90px;
		padding-left: 10px;
		margin: 4px;
		border-radius: 4px;
		font-size: 12px;
		-moz-box-shadow: inset 0 0 10px #CCC;
		-webkit-box-shadow: inset 0 0 10px #CCC;
		box-shadow: inset 0 0 10px #CCC;
	}
	
	//头像
	.icon{
		width: 30px;
		height: 30px;
		margin-right: 4px;
		border-radius: 3px;
		-moz-box-shadow:0 0 1px 1px #06c;
		-webkit-box-shadow:0 0 1px 1px #06c;
		box-shadow:0 0 1px 1px #06c;
	}
	//删除按钮
	.deletebutton{
		width: 30px;
		height: 23px;
		margin-right: 4px;
		background-color: #ff5500;
		font-size: 12px;
	}
	//音频播放
	.audioSetting{
		flex-direction: row;
		display: flex;
	}
	//play图标
	.playIcon{
		width: 20px;
		height: 20px;
	}
	//进度条
	.processorBar{
		margin-left: 4px;
		width: 50%;
	}
	//列表栏的父容器
	.fatherVessel{
		font-size: 12px;
		width: 100%;
		height:100%;
	}
	//第三栏即编辑评论栏
	.editBar{
		flex-direction: row;
		display: flex;
	}
	
	//顶栏显示栏
	.topBar{
		flex-direction: column;
		display: flex;
	}
	//点赞数
	.likes{
		color: #2B85E4;
		margin-left: 5px;
	}
	
	//模块标题
	.title{
		width: 100%;
		height: 50px;
		padding-left: 20px;
		font-size: 14px;
		flex-direction: row; 
		align-items: center;
		border-radius: 4px;
		display: flex;
		align-content: center;
		background-color: #2979FF;
	}
	//编辑评论
	.editComment{
		font-size: 12px;
		color: #2B85E4;
		margin-left: 4px;
	}
	//评论时间
	.commentTime{
		font-size: 12px;
	}
	
	//显示评论
	.allComment{
		width: 90%;
		height: 30px;
		padding-left: 20px;
		font-size: 14px;
		padding-top: 5px;
		margin-top: 10px;
		border-radius: 4px;
		display: flex;
		align-content: center;
		background-color: #55ffff;
	}
	//热门评论标题
	.titleComment{
		font-size: 14px;
	}
	
	//操作条
	.opBar{
		width: 90%;
		height: 30px;
		font-size: 12px;
		padding-top: 5px;
		border-radius: 4px;
		display: flex;
		justify-content: flex-end;
		background-color: #f0f0f0;
		-moz-box-shadow: inset 0 0 10px #CCC;
		-webkit-box-shadow: inset 0 0 10px #CCC;
		box-shadow: inset 0 0 10px #CCC;
	}
	//操作条文本
	.giveComment{
		color: #2B85E4;
		margin-right: 20px;
	}
</style>
