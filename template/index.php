<!DOCTYPE html>
<html lang="en">
	<!-- BEGIN HEAD -->
	<head>
	<?php include "layout/head.html"; ?>
	</head>
	<!-- END HEAD -->

	<body class="page-header-fixed page-sidebar-closed-hide-logo">
		<!-- BEGIN CONTAINER -->
		<div class="wrapper">
			<!-- BEGIN HEADER -->
			<header class="page-header">
				<nav class="navbar mega-menu" role="navigation">
					<div class="container-fluid">
						<?php include "layout/header.html"; ?>
						<!-- BEGIN HEADER MENU -->
						<div class="nav-collapse collapse navbar-collapse navbar-responsive-collapse">
							<?php include "layout/menu.html"; ?>
						</div>
						<!-- END HEADER MENU -->
					</div>
					<!--/container-->
				</nav>
			</header>
			<!-- END HEADER -->
			<div class="container-fluid">
				<div class="page-content">
					<!-- BEGIN BREADCRUMBS -->
					<div class="breadcrumbs">
						<h1>Dashboard</h1>
						<ol class="breadcrumb">
							<li>
								<a href="#">Home</a>
							</li>
							<li class="active">Dashboard</li>
						</ol>
					</div>
					<!-- END BREADCRUMBS -->
					<!-- BEGIN PAGE BASE CONTENT -->
						<?php include "layout/content.html"; ?>
					<!-- END PAGE BASE CONTENT -->
				</div>
				<!-- BEGIN FOOTER -->
				<p class="copyright">2016 © Musrenbang by Smartplan
					
				</p>
				<a href="#index" class="go2top">
					<i class="icon-arrow-up"></i>
				</a>
				<!-- END FOOTER -->
			</div>
		</div>
		<!-- END CONTAINER -->
		
		<!-- END QUICK SIDEBAR -->
		<!--[if lt IE 9]>
<script src="static/assets/global/plugins/respond.min.js"></script>
<script src="static/assets/global/plugins/excanvas.min.js"></script> 
<![endif]-->
		<?php include "layout/bottom.html"; ?>
	</body>

</html>