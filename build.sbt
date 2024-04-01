import scala.sys.process._
// OBS: sbt._ has also process. Importing scala.sys.process
// and explicitly using it ensures the correct operation

ThisBuild / scalaVersion     := "2.13.8"
ThisBuild / version          := scala.sys.process.Process("git rev-parse --short HEAD").!!.mkString.replaceAll("\\s", "")+"-SNAPSHOT"
ThisBuild / organization     := "Chisel-blocks"

val chiselVersion = "3.5.1"

lazy val asyncqueue = (project in file("."))
  .settings(
    name := "asyncqueue",
    libraryDependencies ++= Seq(
      //"org.chipsalliance" %% "chisel" % chiselVersion,
      "edu.berkeley.cs" %% "chisel3" % chiselVersion,
    ),
    scalacOptions ++= Seq(
      "-language:reflectiveCalls",
      "-deprecation",
      "-feature",
      "-Xcheckinit",
      "-Ymacro-annotations",
    ),
    addCompilerPlugin("edu.berkeley.cs" % "chisel3-plugin" % chiselVersion cross CrossVersion.full),
  )
