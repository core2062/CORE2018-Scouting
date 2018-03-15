<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
		<title>CORE 2062 Scouting</title>
		<link rel="shortcut icon" href="favicon.ico" />
		<meta name="description" content="CORE 2062 Scouting Form">
    	<meta name="author" content="CORE2062">
    	<meta name="robots" content="noindex, nofollow">

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" />

		<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity="sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation/foundation.accordion.min.js" integrity="sha256-Sf8QyM10GIsdziOWIIfN7V/ah4iRxPt17tvNCHorXjc=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation/foundation.tab.min.js" integrity="sha256-Qyd0HGGzEOB/qkGWHkxliFbXHCjs2VRDm8mzHEwphzk=" crossorigin="anonymous"></script>

		<script src="https://cdnjs.cloudflare.com/ajax/libs/awesomplete/1.1.1/awesomplete.min.js" integrity="sha256-hQ2PYbQiQS3xeguwt5BS+AMzn5V5JJ0P1kQnuoXdTnk=" crossorigin="anonymous"></script>

		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/awesomplete/1.1.1/awesomplete.min.css" integrity="sha256-pMulKeKs7Hns5vhu0uluhawM68QSrKg/dFfttaXCKE8=" crossorigin="anonymous" />

		<script src="https://cdnjs.cloudflare.com/ajax/libs/parsley.js/2.6.2/parsley.min.js" integrity="sha256-QKOftzbqahZaXS2amOh27JacZ6TbmT4TmGxNo4Jue4Y=" crossorigin="anonymous"></script>

		<script type="text/javascript" src="show.js?v=1"></script>

	</head>
	<body>

		<form name="main" id="form" action="COREDataEntry.py" method="post" data-parsley-validate>
			<div class="row">
				<div class="small-12 columns">
					<ul class="tabs show-for-medium-up" data-tab>
						<li class="tab-title active"><a href="#panel1">Match/Scout Info</a></li>
      					<li class="tab-title"><a href="#panel2">Autonomous Period</a></li>
      					<li class="tab-title"><a href="#panel3">Teleoperated Period</a></li>
      				</ul>
      				<dl class="accordion" data-accordion>
      					<dd class="accordion-navigation">
      					
      					<a href="#panel1" class="show-for-small-only">Match/Scout Info</a>
      						<div id="panel1" class="content active">
      							<div class="content-box section-box">
      								<div class="row">
      									<div class="small-12 columns">
      										<label>Match Number: *
												<input  name="MatchNumber" class="form-control" type="number" placeholder="1" value="<?php echo $_GET['match']; ?>" required="" readonly/>
											</label>
										</div>
									</div>

									<div class="row">
										<div class="small-12 columns">
											<label>Team Number: *
												<input name="TeamNumber" class="form-control" value="<?php echo $_GET['team']; ?>" required="" placeholder="2062" readonly/>
											</label>
										</div>
									</div>

									<div class="row">
										<div class="small-12 columns">
											<label>Scout Name: *
												<input name="ScoutName" placeholder="John Smith" autocomplete="off" data-parsley-required="true"/>
											</label>
										</div>
									</div>
								</div>
							</div>

							<a href="#panel2" class="show-for-small-only">Autonomous Period</a>
	        					<div id="panel2" class="content">
	        						<div class="content-box section-box">
                                        <div class="row">
                                    		<fieldset class="large-6 columns">
                                        	<legend>Crossed Auto Line:</legend>
                                         		<input name="CrossedBaselineAuto" id="CrossedBaseline" value="CrossedBaseLine" type="checkbox"><label for="CrossedBaseline">Yes</label>
                                    		</fieldset>
                                        </div>
      									<div class="row">
      										<fieldset class="large-6 columns">
      										<legend>Delivered Cube in Switch:</legend>
      										 	<input onclick="EnableAutoGearStatus()"  name=								"CubeSwitchAuto" id="LeftSwitchAuto" value="LeftSwitchAuto" type="radio"><label for="LeftSwitchAuto">			Left</label>
      										 	<input required="" onclick="EnableAutoGearStatus()" name="CubeSwitchAuto" id="RightSwitchAuto" value="RightSwitchAuto" type="radio"><label for="RightSwitchAuto">Right</label>
      										 	<input required="" onclick="EnableAutoGearStatus()" name="CubeSwitchAuto" id="FailedSwitchAuto" value="FailedSwitchAuto" type="radio"><label for="FailedSwitchAuto">Fail</label>
       										 	<input required="" onclick="DisableAutoGearStatus()" name="CubeSwitchAuto" id="NoAttempt" value="NoAttempt" type="radio"><label for="NoAttempt">No Attempt</label>
      										</fieldset>
                        				</div>

                                        <div class="row">
      										<fieldset class="large-6 columns">
                                                <legend>Delivered Cube in Scale:</legend>
                                                    <input onclick="EnableAutoGearStatus()"  name=								"CubeScaleAuto" id="LeftScaleAuto" value="LeftScaleAuto" type="radio"><label for="LeftScaleAuto">Left</label>
                                                    <input required="" onclick="EnableAutoGearStatus()" name="CubeScaleAuto" id="RightScaleAuto" value="RightScaleAuto" type="radio"><label for="RightScaleAuto">Right</label>
                                                    <input required="" onclick="EnableAutoGearStatus()" name="CubeScaleAuto" id="FailedScaleAuto" value="FailedScaleAuto" type="radio"><label for="FailedScaleAuto">Fail</label>
                                                    <input required="" onclick="DisableAutoGearStatus()" name="CubeScaleAuto" id="NoAttempt" value="NoAttempt" type="radio"><label for="NoAttempt">No Attempt</label>
      										</fieldset>
                        				</div>
                                        <div class="row">
                                            <fieldset class="large-6 columns">
                                                <legend>Delivered in Exchange</legend>
                                                 <input onclick="EnableAutoExchangeStatus()"  name=                              "CubeExchangeAuto" id="ExchangeAuto" value="ExchangeAuto" type="radio"><label for="ExchangeAuto">Yes</label>
                                                    <input required="" onclick="DisableAutoExchangeStatus()" name="CubeExchangeAuto" id="NoAttempt" value="NoAttempt" type="radio"><label for="NoAttempt">No</label>
                                                    <input required="" onclick="EnableExchangeStatus()" name="CubeExchangeAuto" id="FailedExchangeAuto" value="FailedExchangeAuto" type="radio"><label for="FailedExchangeAuto">Fail</label>
      										</fieldset>
                                        </div>
      								</div>
      							</div>




      					<a href="#panel3" class="show-for-small-only">Teleoperated Period</a>
      						<div id="panel3" class="content">
      							<div class="content-box section-box">

                   					<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          						<label>Cubes Delivered to Own Switch:</label>
                        							<div class="small-4 columns">

                          								<input required type='button' class="button postfix" onclick='document.getElementById("OwnSwitchCubesDelivered").stepDown(1);' value='-'/>
                        							</div>
                        							<div class="small-4 columns">
                           					 			<input required type="number" name="OwnSwitchCubesDelivered" id="OwnSwitchCubesDelivered" min="0" step="1" value ="0" required readonly>
                        							</div>
                        							<div class="small-4 columns">
                          								<input required type='button' class="button postfix" onclick='document.getElementById("OwnSwitchCubesDelivered").stepUp(1);' value='+'/>
                        							</div>
                      							</div>
                   				 			</div>
                  						</div>

									<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                          				<label>Cubes Delivered to Scale:</label>
                        				<div class="small-4 columns">
                          					<input required type='button' class="button postfix" onclick='document.getElementById("ScaleCubesDelivered").stepDown(1);' value='-'/>
                        				</div>
                        				<div class="small-4 columns">
                           					 <input required type="number" name="ScaleCubesDelivered" id="ScaleCubesDelivered" min="0" step="1" value ="0" required readonly>
                        				</div>
                        				<div class="small-4 columns">
                          				<input required type='button' class="button postfix" onclick='document.getElementById("ScaleCubesDelivered").stepUp(1);' value='+'/>
                        				</div>
                      				</div>
                   				 </div>
                  				</div>


                   					<div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                                                <label>Cubes Delivered to Opposing Switch:</label>
                                                <div class="small-4 columns">
                                                    <input required type='button' class="button postfix" onclick='document.getElementById("OpposingSwitchCubesDelivered").stepDown(1);' value='-'/>
                                                </div>
                                                <div class="small-4 columns">
                                                     <input required type="number" name="OpposingSwitchCubesDelivered" id="OpposingSwitchCubesDelivered" min="0" step="1" value ="0" required readonly>
                                                </div>
                                                <div class="small-4 columns">
                                                <input required type='button' class="button postfix" onclick='document.getElementById("OpposingSwitchCubesDelivered").stepUp(1);' value='+'/>
                                                </div>
                                 			</div>
                   				 		</div>
                  					</div>
                                    <div class="row">
                    					<div class="large-12 columns">
                      						<div class="row collapse">
                                                <label>Cubes Delivered to Exchange:</label>
                                                <div class="small-4 columns">
                                                    <input required type='button' class="button postfix" onclick='document.getElementById("ExchangeCubesDelivered").stepDown(1);' value='-'/>
                                                </div>
                                                <div class="small-4 columns">
                                                     <input required type="number" name="ExchangeCubesDelivered" id="ExchangeCubesDelivered" min="0" step="1" value ="0" required readonly>
                                                </div>
                                                <div class="small-4 columns">
                                                <input required type='button' class="button postfix" onclick='document.getElementById("ExchangeCubesDelivered").stepUp(1);' value='+'/>
                                                </div>
                                 			</div>
                   				 		</div>
                  					</div>
                  				</fieldset>
      							<div class="row">
      									<fieldset class="large-12 columns">

      										<legend>Cube Manipulation:</legend>

      										 <input name="CubeFloorPickup" id="CubeFloorPickup" type="checkbox"><label for="CubeFloorPickup">Cube Floor Pickup?</label>

      										<legend>Cube Handling Type:</legend>
      										 <input required="" name="GearFloorPickupType" id="ActivePickup" value="Active" type="radio"><label for="ActivePickup">Active</label>
      										  <input required="" name="GearFloorPickupType" id="PassivePickup" value="Passive" type="radio"><label for="PassivePickup">Passive</label>
      										  <input required="" name="GearFloorPickupType" id="NoPickup" value="None" type="radio"><label for="NoPickup">None</label>
      									</fieldset>
      								</div>
								</div>
								<fieldset>
                                    <legend>Climbing:</legend>
                                    <div class="row">
                                        <input required="" name="Climb" id="NoClimb" value="NoClimb" type="radio"><label for="NoClimb">No Climb</label>
                                        <input required="" name="Climb" id="DidClimb" value="DidClimb" type="radio"><label for="DidClimb">Successful Climb</label>
                                        <input required="" name="Climb" id="ClimbPark" value="ClimbPark" type="radio"><label for="ClimbPark">Parked</label>
                                        <input required="" name="Climb" id="ClimbLevitate" value="ClimbLevitate" type="radio"><label for="ClimbLevitate">Levitated</label>
                                        <input required="" name="Climb" id="ClimbFail" value="ClimbFail" type="radio"><label for="ClimbFail">Failed Climb</label>
                                    </div>
								</fieldset>
                                <div class="row">
                                    <input name="ClimbAssist" id="ClimbAssist" type="checkbox"><label for="ClimbAssist">Climb Assist?</label>
                                </div>
                                <div class="row">
                                    <fieldset class="large-6 columns">
                                        <legend>Defense:</legend>
                       <input required="" name="Defense" id="NotGreat" value="NotGreat" type="radio"><label for="NotGreat">Not Great</label>
                       <input required="" name="Defense" id="Alright" value="Alright" type="radio"><label for="Alright">Alright</label>
                       <input required="" name="Defense" id="Good" value="Good" type="radio"><label for="Good">Good</label>
                       <input required="" name="Defense" id="Amazing" value="Amazing" type="radio"><label for="Amazing">Amazing</label>
                       <input required="" name="Defense" id="DefenseNone" value="None" type="radio"><label for="DefenseNone">None</label>
                                    </fieldset>
                                </div>
      						</div>
                            <div class="row">
                            <div class="large-12 columns">
                            <label>Comments
                                <textarea name="comments" placeholder=""></textarea>
                            </label>
                            </div>
							<input class="button round SubmitButton" type="submit" value="Submit">
					</dl>
        </form>
<script>
      $(document).foundation();
</script>
<script type="text/javascript">
  $('#form').parsley();
</script>
	</body>
</html>     												