1. 라이다의 laser 데이터를 python 으로 plot 하기 위한 코드 입니다.
2. 
rostopic list # 가제보 topic list
rostopic echo * # 토픽 보기
rostopic type * # 토픽 타입보기 ex input) odom, scan
rosmsg show *  # 메세지 타입보기 ex input) nav_msgs/Odometry
rosrun tf view_frames # tf 그래프 출력
evince frames.pdf # tf 그래프 보기

위의 방법으로 데이터 형태 뽑아 냅니다.
를
3. 실행 : roslaunch rospy_scan scan.launch 
