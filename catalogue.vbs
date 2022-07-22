Const OutputPath = "C:\output.txt"
Const BeginFolder  = "C:\testFolder"
 
Dim FSO, TheFolder, F
Set FSO = CreateObject("Scripting.FileSystemObject")
Set TheFolder = FSO.GetFolder(BeginFolder)
 
On Error Resume Next
set F = Fso.CreateTextFile(OutputPath)
F.Close()
 
set F = Fso.OpenTextFile(OutputPath, 8, true)
WorkWithSubFolders TheFolder
F.Close()
Msgbox "End!"
 
 
Sub WorkWithSubFolders(ByVal AFolder)
  Dim MoreFolders, TempFolder
 
  F.WriteLine(AFolder.Path & "\")
  
  If AFolder.Name = "System Volume Information" Then Exit Sub
 
  Set MoreFolders = AFolder.SubFolders
  For Each TempFolder In MoreFolders
    WorkWithSubFolders TempFolder
  Next
End Sub